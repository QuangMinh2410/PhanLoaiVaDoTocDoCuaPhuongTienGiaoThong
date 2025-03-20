**Phân Loại Và Đo Tốc Độ Của Phương Tiện Giao Thông**  
_Đề tài áp dụng mạng học sâu (YOLO) và xử lý video để phát hiện, phân loại phương tiện và tính toán tốc độ di chuyển từ dữ liệu hình ảnh._

---

### 🌟 **Giới thiệu**  
- **Phân loại phương tiện:** Sử dụng mô hình YOLO để nhận diện các loại phương tiện giao thông như xe hơi, xe tải.  
- **Đo tốc độ:** Tính toán vận tốc của phương tiện dựa trên khoảng cách pixel trong hình ảnh kết hợp thông số thực tế.  
- **Ứng dụng:** Phân luồng giao thông, giám sát vi phạm, hỗ trợ quản lý đô thị.

---

### 🏗️ **Hệ thống**  
#### 📂 **Cấu trúc dự án**  
📦 Project  
├── 📂 VehicleDetection # Chứa mã nguồn YOLO và xử lý tốc độ  
│ ├── detect_and_classify_vehicles.py # Module chính triển khai thuật toán  
├── 📂 models  
│ ├── yolov8n.pt # Mô hình YOLO được huấn luyện trước  
├── 📂 input_videos  
│ ├── traffic_video.mp4 # Video mẫu  
├── 📂 output_videos  
│ ├── detected_output.mp4 # Video đầu ra sau khi xử lý  
├── run.py # Tập lệnh chính chạy chương trình  

---

### 🛠️ **Công nghệ sử dụng**  
#### 📡 **Phần cứng**  
- **Camera:** Thu thập dữ liệu hình ảnh phương tiện.  
- **Thiết bị xử lý:** Máy tính hỗ trợ xử lý dữ liệu hình ảnh trong thời gian thực.  

#### 🖥️ **Phần mềm**  
- **Python (OpenCV):** Tiền xử lý video, hiển thị kết quả.  
- **Ultralytics YOLO:** Mô hình học sâu chuyên nhận diện đối tượng.  

---

### 🧮 **Thuật toán**
1. **Phân loại phương tiện:**
   - Dựa trên mô hình YOLO (`yolov8n.pt`) để phát hiện bounding box và phân loại đối tượng (xe hơi, xe tải, ...).
2. **Đo tốc độ:**
   - Tính vận tốc dựa vào:
     - **Khoảng cách pixel:** Tính từ bounding box giữa hai khung hình.
     - **Thông số thực tế:** Chuyển đổi pixel sang mét bằng `real_distance_per_pixel`.
   - Công thức chuyển đổi:  
   Tốc độ(km/h) = (Khoảng cách thực(m) / (Thời Gian(s)) * 3.6
3. **Hiển thị kết quả:**
   - Bounding box được tô màu:
     - **Xanh lá cây:** Nếu tốc độ phương tiện ≤ ngưỡng cho phép (80 km/h).  
     - **Đỏ:** Nếu vượt ngưỡng.  

---

### 🚀 **Hướng dẫn cài đặt và chạy**  
1️⃣ **Cài đặt môi trường:**  
```bash
pip install ultralytics opencv-python
```

2️⃣ **Chạy chương trình chính:**  
```bash
python Nhom6_PhanLoaiVaDoTocDoCuaPhuongTienGiaoThong.py
```

3️⃣ **Kết quả:**  
- Video đầu ra hiển thị bounding box và tốc độ từng phương tiện được lưu vào `output_videos`.

---

### 📖 **Hướng dẫn sử dụng**
1️⃣ **Nhập video giao thông:**  
- Lưu video vào thư mục `input_videos` và cập nhật đường dẫn trong mã nguồn.

2️⃣ **Xem kết quả:**  
- Kết quả xuất hiện trên cửa sổ hiển thị hoặc được lưu tự động dưới dạng video đầu ra.

3️⃣ **Cấu hình thông số:**  
- Thay đổi ngưỡng tốc độ (`SPEED_LIMIT`) và khoảng cách thực tế mỗi pixel (`real_distance_per_pixel`) trong mã nguồn.

---

### 🔧 **Ghi chú**
- **Cổng camera:** Đảm bảo cấu hình đúng khi thu thập video trong thực tế.  
- **Mô hình YOLO:** Có thể thay thế bằng các biến thể khác như YOLOv5 hoặc YOLOv4 tùy theo yêu cầu.  

---

### 🤝 **Đóng góp nhóm**  
| Họ và Tên         | Vai trò                                                                         |  
|-------------------|---------------------------------------------------------------------------------|  
| Đỗ Quang Minh     | Phát triển thuật toán phát hiện và đo tốc độ. Viết báo cáo và thiết kế tài liệu.|  
| Nguyễn Hữu Bảo    | Tiền xử lý dữ liệu và kiểm thử hệ thống. Tích hợp YOLO và tối ưu mã nguồn.      |  
| Lê Thái Dương     |  Thiết kế slide PowerPoint, hỗ trợ bài tập lớn.                                 |  

---

© 2025 NHÓM AI-1, TRƯỜNG ĐẠI HỌC TRÍ TUỆ NHÂN TẠO  

Nếu bạn cần hỗ trợ cụ thể hơn hoặc muốn sửa đổi thêm, hãy nói tôi nhé! 😊
