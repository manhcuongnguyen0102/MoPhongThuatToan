# MoPhongThuatToan
# 📊 Algorithm Visualizer (Mô Phỏng Thuật Toán Sắp Xếp)

Dự án ứng dụng giao diện đồ họa (GUI) sử dụng Python và PyQt5 để trực quan hóa quá trình hoạt động của các thuật toán sắp xếp kinh điển. Ứng dụng cho phép người dùng quan sát theo thời gian thực sự dịch chuyển của từng phần tử dữ liệu thông qua các cột biểu đồ động.

## 🛠 Công nghệ & Kiến trúc
* **Ngôn ngữ:** Python 3.x
* **Giao diện:** PyQt5 (QtWidgets, QtGui, QtCore)
* **Kiến trúc (Software Architecture):** Áp dụng triệt để tư duy tách biệt (Separation of Concerns). 
  * Lớp Giao diện (`graph.py`, `main.py`) chỉ chịu trách nhiệm vẽ đồ họa.
  * Lớp Nghiệp vụ (`quickSort.py`, `MergeSort.py`, `HeapSort.py`) hoàn toàn độc lập, không chứa code UI.
  * Hai lớp giao tiếp với nhau thông qua kỹ thuật **Callback Function** (`draw_func`).

## 🧠 Kiến thức Trọng tâm Kỹ thuật

### 1. Xử lý Sự kiện (Event Handling) & Tối ưu Nút bấm
* Sử dụng `lambda` hoặc `functools.partial` trong hàm `.connect()` để giải quyết 2 bài toán cốt lõi:
  * Tránh lỗi **Thực thi ngay lập tức (Immediate Execution)** khi cần truyền tham số dạng chuỗi (ví dụ: chuyển trang theo tên thuật toán).
  * Làm **lá chắn tham số**, ngăn chặn tín hiệu `False` mặc định của sự kiện `clicked` vô tình ghi đè vào kích thước mảng khiến hệ thống sinh ra mảng rỗng `[]`.

### 2. Đồ họa Hướng sự kiện (Event-Driven Graphics)
* **Cơ chế QPainter:** Cây cọ đồ họa chỉ được phép khởi tạo và hoạt động bên trong hàm `paintEvent(self, event)`. Lập trình viên không bao giờ gọi trực tiếp hàm này.
* **Vòng lặp Render:** Khi mảng dữ liệu thay đổi, lệnh `self.update()` được phát ra để báo hiệu cho hệ điều hành lên lịch gọi hàm `paintEvent` vẽ lại khung hình mới.
* **Tô nền thủ công:** Khi ghi đè `paintEvent`, tính năng tự động tô màu nền bị vô hiệu hóa. Bắt buộc phải sử dụng `painter.fillRect(self.rect(), QColor("black"))` để chủ động phủ lớp nền trước khi vẽ các cột.

### 3. Điều hướng Hoạt hình (Animation Loop)
Để tránh hiện tượng ứng dụng bị đóng băng (Not Responding) do thuật toán tính toán quá nhanh, vòng lặp hoán vị sử dụng combo 3 lệnh:
1. `self.update()`: Đặt lịch vẽ đồ thị mới.
2. `QApplication.processEvents()`: Ép luồng chính (Main Thread) đẩy ngay đồ thị lên màn hình.
3. `time.sleep(0.05)`: Đóng băng hệ thống 50ms tạo ra các khung hình (frames) mượt mà cho mắt người.

## 🐛 Sổ tay Khắc phục Lỗi (Troubleshooting)

| Vấn đề gặp phải | Nguyên nhân Kỹ thuật | Giải pháp Áp dụng |
| :--- | :--- | :--- |
| **Bảng vẽ không có màu nền đen** | Ghi đè `paintEvent` làm mất lệnh CSS `background-color` mặc định của QWidget. | Thêm lệnh `fillRect` bằng QPainter ở ngay dòng đầu tiên của sự kiện vẽ. |
| **Màu đồ thị hòa lẫn vào nền** | PyQt5 sử dụng thang màu HSL/RGB từ `0-255`, nhưng bị nhầm sang hệ `% (0-100)` của Web CSS. | Chuyển đổi thông số sang hệ 255 hoặc dùng tên màu định nghĩa sẵn (VD: `lightgreen`). |
| **Mất số đầu tiên ở mảng** | Vòng lặp lùi `range(n, 0, -1)` dừng lại khi chạm mức 0 (Exclusive stop). | Đẩy điểm dừng xuống `-1` (`range(n, -1, -1)`) để lấy được chỉ số `0` (đỉnh Heap). |
| **Nút bấm sinh ra mảng rỗng** | `clicked` emit tham số `False` đè vào kích thước `size=50` (False = 0). | Bọc lệnh gọi bằng `lambda: self.gen_arr()`. |