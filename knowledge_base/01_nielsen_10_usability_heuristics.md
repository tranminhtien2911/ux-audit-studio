# 10 NGUYÊN LÝ KHẢ DỤNG GIAO DIỆN CỦA JAKOB NIELSEN (NN/G 10 USABILITY HEURISTICS)
Nguồn: Nielsen Norman Group (Jakob Nielsen)

## 1. Hiển thị trạng thái hệ thống (Visibility of system status)
- Thiết kế phải luôn thông báo cho người dùng biết chuyện gì đang xảy ra, thông qua phản hồi thích hợp trong khoảng thời gian hợp lý.
- **Tiêu chí kiểm toán:**
  - Có thanh tiến trình (Progress bar) hoặc vòng xoay tải (Loading spinner) khi tải dữ liệu > 1 giây không?
  - Trạng thái hoàn thành/thất bại có hiển thị rõ bằng Toast thông báo hoặc Modal không?
  - Vị trí hiện tại của người dùng có được làm nổi bật (Active nav indicator, Breadcrumbs) không?

## 2. Tương thích giữa hệ thống và thế giới thực (Match between system and real world)
- Hệ thống phải nói ngôn ngữ của người dùng, sử dụng từ ngữ, cụm từ và khái niệm quen thuộc, tuân theo quy ước thế giới thực.
- **Tiêu chí kiểm toán:**
  - Biểu tượng (Icon) có mang ý nghĩa phổ quát (Kính lúp = Tìm kiếm, Thùng rác = Xóa, Bánh răng = Cài đặt) không?
  - Tránh dùng thuật ngữ kỹ thuật khó hiểu (như "Error code 500", "Null pointer", "Payload invalid").

## 3. Quyền kiểm soát và tự do của người dùng (User control and freedom)
- Người dùng thường thực hiện hành động do nhầm lẫn. Họ cần một "lối thoát khẩn cấp" rõ ràng để rời khỏi trạng thái không mong muốn mà không phải trải qua quy trình phức tạp.
- **Tiêu chí kiểm toán:**
  - Có nút "Hủy" (Cancel), "Quay lại" (Back), hoặc "Đóng" (X) rõ ràng không?
  - Có tính năng Hoàn tác (Undo) hoặc Xác nhận (Confirmation) cho các hành động nguy hiểm không?

## 4. Nhất quán và tuân thủ tiêu chuẩn (Consistency and standards)
- Người dùng không cần phải tự hỏi liệu các từ ngữ, tình huống hoặc hành động khác nhau có cùng ý nghĩa hay không (Định luật Jakob).
- **Tiêu chí kiểm toán:**
  - Màu sắc ngữ nghĩa có nhất quán (Đỏ = Nguy hiểm/Xóa, Xanh lá = Thành công, Xanh dương = Tương tác) không?
  - Nút bấm chính (Primary action) có đồng nhất vị trí trên mọi màn hình không?

## 5. Phòng ngừa lỗi (Error prevention)
- Thiết kế tốt nhất là ngăn chặn lỗi xảy ra ngay từ đầu, thay vì hiển thị thông báo lỗi đẹp mắt.
- **Tiêu chí kiểm toán:**
  - Có vô hiệu hóa (disabled) nút bấm khi form chưa điền đủ thông tin hợp lệ không?
  - Có định dạng sẵn (mask) cho số điện thoại, ngày tháng, tiền tệ không?
  - Có cảnh báo xác nhận trước khi xóa dữ liệu vĩnh viễn không?

## 6. Nhận biết thay vì nhớ lại (Recognition rather than recall)
- Giảm thiểu tải bộ nhớ của người dùng bằng cách làm cho các phần tử, hành động và tùy chọn luôn nhìn thấy được.
- **Tiêu chí kiểm toán:**
  - Ô tìm kiếm có gợi ý lịch sử tìm kiếm và autocomplete không?
  - Form nhập liệu có hiển thị rõ nhãn (Floating label) chứ không chỉ dựa vào placeholder bị biến mất khi gõ không?

## 7. Linh hoạt và hiệu quả sử dụng (Flexibility and efficiency of use)
- Giao diện phục vụ tốt cả người dùng mới và người dùng chuyên nghiệp (Power users).
- **Tiêu chí kiểm toán:**
  - Có phím tắt (Keyboard shortcuts) hoặc thao tác hàng loạt (Bulk actions) cho bảng dữ liệu không?
  - Có các bộ lọc nhanh (Quick filters) cho danh sách dài không?

## 8. Thiết kế thẩm mỹ và tối giản (Aesthetic and minimalist design)
- Giao diện không nên chứa thông tin không liên quan hoặc hiếm khi cần thiết. Mỗi đơn vị thông tin thừa đều làm giảm độ nổi bật của thông tin quan trọng.
- **Tiêu chí kiểm toán:**
  - Tỷ lệ khoảng trắng (White space) có cân đối, tránh nhồi nhét chữ và nút bấm không?
  - Phân cấp thị giác (Typography & Visual hierarchy) có làm nổi bật thông điệp chính không?

## 9. Giúp người dùng nhận biết, chẩn đoán và khắc phục lỗi (Help users recognize and recover from errors)
- Thông báo lỗi phải bằng ngôn ngữ đời thường (không có mã lỗi), chỉ rõ vấn đề và đề xuất giải pháp khắc phục mang tính xây dựng.
- **Tiêu chí kiểm toán:**
  - Thông báo lỗi form có nằm ngay cạnh trường bị lỗi (Inline validation) không?
  - Nội dung lỗi có chỉ rõ cần làm gì (ví dụ: "Mật khẩu cần tối thiểu 8 ký tự" thay vì "Mật khẩu không hợp lệ") không?

## 10. Trợ giúp và tài liệu (Help and documentation)
- Mặc dù hệ thống nên trực quan mà không cần tài liệu, việc cung cấp gợi ý (Tooltip, Help text) ngắn gọn tại chỗ là vô cùng hữu ích.
