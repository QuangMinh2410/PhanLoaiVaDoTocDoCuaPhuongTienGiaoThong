from ultralytics import YOLO
import cv2
import time

# Định nghĩa màu sắc
RED_COLOR = (0, 0, 255)  # Vượt quá tốc độ
GREEN_COLOR = (0, 255, 0)  # Đúng tốc độ

# Tốc độ mặc định nếu không tính được (km/h)
DEFAULT_SPEED = 60

# Ngưỡng tốc độ tối đa (km/h)
SPEED_LIMIT = 80

def detect_and_classify_vehicles(video_path, real_distance_per_pixel, model_path="yolov8n.pt"):
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Không thể mở video. Vui lòng kiểm tra đường dẫn.")
        return

    # Lưu thông tin về phương tiện
    vehicle_data = {}
    fixed_speeds = {}

    # Lấy FPS của video để tính toán khoảng thời gian giữa các frame
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = max(1, int(fps / 10))  # Xử lý mỗi 1/10 số frame
    frame_id = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Đã xử lý hết video hoặc có lỗi khi đọc frame.")
            break

        frame_id += 1
        if frame_id % frame_interval != 0:
            continue

        current_time = time.time()
        results = model(frame)

        for result in results:
            boxes = result.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cls = int(box.cls)
                label = model.names[cls]

                if label.lower() in ['car', 'truck']:
                    object_id = f"{label} ID:{x1+y1+x2+y2}"

                    # Lưu vị trí & thời gian của phương tiện
                    if object_id not in vehicle_data:
                        vehicle_data[object_id] = []
                    vehicle_data[object_id].append((x1, y1, current_time))

                    # Tính toán tốc độ
                    if object_id not in fixed_speeds and len(vehicle_data[object_id]) >= 2:
                        x1_prev, y1_prev, time_prev = vehicle_data[object_id][-2]
                        x1_curr, y1_curr, time_curr = vehicle_data[object_id][-1]
                        time_diff = time_curr - time_prev

                        if time_diff > 0:
                            pixel_distance = ((x1_curr - x1_prev) ** 2 + (y1_curr - y1_prev) ** 2) ** 0.5
                            real_distance = pixel_distance * real_distance_per_pixel
                            speed = (real_distance / time_diff) * 3.6  # m/s → km/h
                            fixed_speeds[object_id] = speed

                    # Lấy vận tốc, nếu chưa có thì dùng tốc độ mặc định
                    speed = fixed_speeds.get(object_id, DEFAULT_SPEED)

                    # Chọn màu dựa trên tốc độ
                    box_color = RED_COLOR if speed > SPEED_LIMIT else GREEN_COLOR

                    # Vẽ bounding box và tốc độ lên frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), box_color, 2)
                    cv2.putText(frame, f"{label} {speed:.2f} km/h", (x1, y1 - 10), 
                                cv2.FONT_HERSHEY_SIMPLEX, 0.9, box_color, 2)

        # Hiển thị frame với thông tin
        cv2.imshow("Detected Video", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Nhấn 'q' để thoát
            break

    cap.release()
    cv2.destroyAllWindows()

# Chạy chương trình với video đã tải lên
if __name__ == "__main__":
    video_path = "traffic_video.mp4"
    real_distance_per_pixel = 0.05  # Khoảng cách thực tế giữa hai điểm (m/pixel)

    print("Đang phát hiện và phân loại phương tiện giao thông từ video...")
    detect_and_classify_vehicles(video_path, real_distance_per_pixel)