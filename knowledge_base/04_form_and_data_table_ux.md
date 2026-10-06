# TIÊU CHUẨN THIẾT KẾ FORM, BỘ LỌC, TÌM KIẾM & BẢNG DỮ LIỆU
Nguồn: Luke Wroblewski (Form Design Best Practices) & Material Design 3 Enterprise UX

## 1. Tiêu chuẩn Thiết kế Form & Ô nhập liệu (Input Fields)
- **1.1 Bố cục cột đơn (Single-column layout):**
  - Form một cột giúp mắt người dùng di chuyển thẳng đứng tự nhiên từ trên xuống dưới, giảm thời gian hoàn thành tới 40% so với form nhiều cột lộn xộn.
- **1.2 Nhãn hiển thị liên tục (Persistent Labels):**
  - TUYỆT ĐỐI không thay thế Label bằng Placeholder. Placeholder sẽ biến mất khi người dùng gõ, làm họ quên mất ô đó yêu cầu thông tin gì. Hãy dùng Top Label hoặc Floating Label.
- **1.3 Xác thực tức thì (Inline Validation):**
  - Kiểm tra tính hợp lệ của trường ngay khi người dùng hoàn thành ô đó (`onBlur`), chứ không đợi bấm nút Submit mới báo một loạt lỗi.
  - Hiển thị dấu tích xanh (✓) cho trường hợp lệ và thông báo lỗi rõ ràng bên dưới trường chưa đạt.
- **1.4 Tối ưu bàn phím trên thiết bị di động:**
  - Ô số điện thoại phải mở bàn phím số (`inputmode="tel"` hoặc `numeric`), ô email mở bàn phím có ký tự `@` và `.com`.

## 2. Tiêu chuẩn Thiết kế Bảng dữ liệu (Data Tables & Lists)
- **2.1 Canh lề chuẩn mực theo loại dữ liệu:**
  - Văn bản (Tên, địa chỉ, email): Canh lề **Trái** (Left-align).
  - Số liệu định lượng (Tiền tệ, số lượng, phần trăm): Canh lề **Phải** (Right-align) để người dùng dễ so sánh độ lớn hàng đơn vị, chục, trăm.
  - Trạng thái (Active, Inactive, Badge): Canh lề **Giữa** (Center-align).
- **2.2 Tránh cắt ngắn thông tin tùy tiện (No Indiscriminate Truncation):**
  - Không cắt dấu ba chấm `...` cho những thông tin quan trọng (Tên người dùng, vai trò, email) nếu chiều rộng cột vẫn còn chỗ trống. Cho phép bọc chữ (Wrap text) hoặc cung cấp Tooltip xem chi tiết khi rê chuột.
- **2.3 Thao tác theo dòng & Thao tác hàng loạt (Row Actions & Bulk Actions):**
  - Với bảng dài, các thao tác nhanh (Chỉnh sửa, Xóa, Copy) phải xuất hiện rõ ràng hoặc xuất hiện khi hover, không giấu quá 3 tầng menu con.
- **2.4 Trạng thái phân trang (Pagination State):**
  - Luôn vô hiệu hóa (disabled / mờ 30%) các nút lùi trang `<` hoặc về đầu trang `|<` khi đang ở trang 1.
  - Hiển thị rõ tổng số bản ghi (ví dụ: "Hiển thị 1-10 trên tổng số 120 kết quả").

## 3. Tiêu chuẩn Trạng thái Trống (Empty States)
- Khi một bảng hoặc danh sách chưa có dữ liệu (hoặc kết quả tìm kiếm rỗng):
  - KHÔNG để màn hình trống trơn hoặc chỉ có một dòng chữ lạnh lùng "Không tìm thấy dữ liệu".
  - PHẢI có: Hình minh họa thân thiện, lời giải thích ngắn gọn lý do, và một Nút hành động cụ thể (ví dụ: "Thêm người dùng đầu tiên", "Xóa bộ lọc để thử lại").
