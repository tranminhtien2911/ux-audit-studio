# TIÊU CHUẨN TIẾP CẬN QUỐC TẾ W3C WCAG 2.2 (ACCESSIBILITY HEURISTICS)
Nguồn: W3C Web Accessibility Initiative (WCAG 2.2 Level AA Standard)

## 1. Nguyên tắc Khả tri (Perceivable - Có thể cảm nhận được)
- **1.1 Độ tương phản màu sắc (Color Contrast - WCAG 1.4.3):**
  - Chữ thông thường: Độ tương phản giữa chữ và nền phải đạt tối thiểu **4.5:1**.
  - Chữ lớn (>=18pt hoặc >=14pt đậm) và thành phần đồ họa (Icon, viền input, nút bấm): Tối thiểu **3.0:1**.
  - Kiểm toán: Không dùng chữ xám nhạt (`#94a3b8`) trên nền trắng cho các thông tin quan trọng.
- **1.2 Không dùng màu sắc làm tín hiệu duy nhất (Use of Color - WCAG 1.4.1):**
  - Trạng thái lỗi không được chỉ đổi màu đỏ mà phải có thêm biểu tượng cảnh báo (!) hoặc thông điệp chữ đi kèm.
  - Trạng thái thành công/kích hoạt phải có icon hoặc nhãn chữ, tránh chỉ dựa vào chấm màu.
- **1.3 Văn bản thay thế (Text Alternatives - WCAG 1.1.1):**
  - Mọi ảnh minh họa, icon chức năng phải có nhãn mô tả (alt text / aria-label).

## 2. Nguyên tắc Vận hành (Operable - Có thể thao tác được)
- **2.1 Kích thước mục tiêu chạm (Target Size Minimum - WCAG 2.5.8):**
  - Kích thước tối thiểu cho mọi phần tử tương tác (Nút bấm, checkbox, radio, icon click được) trên màn hình cảm ứng: **24 x 24 px** (WCAG 2.2 Level AA) và khuyến nghị **44 x 44 px** (theo chuẩn Apple HIG / Google Material).
  - Khoảng cách giữa các nút bấm liền kề phải đủ lớn để tránh bấm nhầm.
- **2.2 Trạng thái chỉ báo tiêu điểm (Focus Visible - WCAG 2.4.7):**
  - Khi người dùng dùng phím Tab hoặc bàn phím ngoài, thành phần đang chọn phải có viền nổi bật (Focus outline rõ ràng), không được tắt `outline: none` mà không có kiểu thay thế.
- **2.3 Không bẫy bàn phím (No Keyboard Trap - WCAG 2.1.2):**
  - Người dùng có thể điều hướng vào và ra khỏi mọi Modal/Popup bằng phím `Tab` hoặc phím `Esc`.

## 3. Nguyên tắc Dễ hiểu (Understandable - Dễ hiểu và dự đoán được)
- **3.1 Nhất quán trong điều hướng (Consistent Navigation - WCAG 3.2.3):**
  - Thanh menu, thanh tìm kiếm và cấu trúc chân trang phải xuất hiện ở cùng một vị trí trên các trang con.
- **3.2 Định danh nhất quán (Consistent Identification - WCAG 3.2.4):**
  - Các thành phần có cùng chức năng phải có cùng tên gọi và biểu tượng trên toàn bộ ứng dụng.
- **3.3 Hướng dẫn nhập liệu và phòng ngừa lỗi (Input Assistance - WCAG 3.3.2 & 3.3.4):**
  - Cung cấp nhãn rõ ràng cho từng ô nhập liệu. Với các giao diện tài chính hoặc giao dịch pháp lý, người dùng phải được xem lại và xác nhận trước khi gửi.

## 4. Nguyên tắc Bền vững (Robust - Tương thích mạnh mẽ)
- Sử dụng mã ngữ nghĩa (Semantic HTML/Components): Nút bấm phải là `<button>`, liên kết là `<a>`, tiêu đề là `<h1>-<h6>`, đảm bảo phần mềm đọc màn hình (Screen Readers) hoạt động chuẩn xác.
