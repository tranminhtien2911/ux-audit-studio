# TIÊU CHUẨN THIẾT KẾ ĐIỀU HƯỚNG & CẢM ỨNG DI ĐỘNG (APPLE HIG & MATERIAL DESIGN 3)
Nguồn: Apple Human Interface Guidelines & Google Material Design 3

## 1. Vùng ngón tay cái (Thumb Zone Navigation)
- Người dùng di động thao tác bằng một tay trong 75% trường hợp.
- **Vùng dễ tiếp cận (Natural Zone):** Nửa dưới màn hình. Đây là nơi đặt Bottom Navigation Bar, Floating Action Button (FAB) và các nút xác nhận chính.
- **Vùng khó tiếp cận (Hard to Reach Zone):** Góc trên cùng bên trái và phải. Chỉ nên đặt các nút phụ hoặc icon xem thông tin.

## 2. Tiêu chuẩn Thanh điều hướng dưới đáy (Bottom Navigation Bar)
- Chỉ chứa từ **3 đến 5 điểm đến chính**. Ít hơn 3 thì nên dùng tab đơn giản, nhiều hơn 5 sẽ gây chật chội và bấm nhầm.
- Điểm đến đang hoạt động (Active tab) phải có sự tương phản vượt trội (Đổi màu, có nền pill bao quanh, hoặc icon tô đậm) so với các tab không hoạt động.
- Tab bar phải cố định (sticky) hoặc ẩn thông minh khi cuộn xuống và hiện lại ngay khi cuộn ngược lên.

## 3. Hệ thống Phân cấp và Điều hướng Đa tầng (Information Architecture & Wayfinding)
- **Quy tắc "You Are Here":**
  - Mọi màn hình đều phải trả lời được câu hỏi: *"Tôi đang ở đâu?"*, *"Tôi từ đâu tới?"*, và *"Tôi có thể đi đâu tiếp theo?"*.
  - Tiêu đề màn hình (Large Title / App Header) phải đồng nhất tuyệt đối với tên mục đã chọn ở màn hình trước.
- **Vụn bánh mì (Breadcrumbs):**
  - Cực kỳ quan trọng cho các ứng dụng web và cổng quản trị (Admin Dashboard). Breadcrumb phải cho phép nhấp vào các cấp cha để quay lại nhanh chóng.
  - Cấp độ hiện tại (cuối cùng) phải được hiển thị dưới dạng văn bản tĩnh (không thể nhấp) để tránh gây nhầm lẫn.

## 4. Phản hồi Xúc giác và Thị giác (Haptics & Micro-interactions)
- Mọi nút bấm khi được chạm (Pressed state) phải có phản hồi thị giác ngay lập tức: Giảm nhẹ độ sáng, gợn sóng (Ripple effect), hoặc hiệu ứng nhấn xuống (Scale 0.98).
- Tuyệt đối không để xảy ra hiện tượng "nút chết" (bấm vào không có bất kỳ phản hồi nào, khiến người dùng bấm liên tục nhiều lần tạo ra trùng lặp giao dịch).
