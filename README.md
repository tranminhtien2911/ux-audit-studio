# 🎨 UX Audit Studio (Pro Edition)

Ứng dụng kiểm toán và phản biện trải nghiệm người dùng (UX/UI Usability Audit) cho các luồng giao diện (UI Flow), vận dụng triệt để hệ thống tri thức và nguyên lý thiết kế từ NotebookLM:
- **Don Norman:** *The Design of Everyday Things* (Tính trực quan, Phản hồi, Affordance, Signifiers, Khoảng cách Thực thi & Đánh giá).
- **Steve Krug:** *Don't Make Me Think* (Định luật tối cao, Tính tự giải thích, Gợi ý clickability, Điều hướng "You are here").
- **Creative Tim:** *Fundamentals of Creating a Great UI/UX*.

---

## 🌐 1. Chế độ Public Web (Truy cập từ bất kỳ đâu qua Internet)

Ứng dụng được tích hợp sẵn đường hầm bảo mật **Cloudflare Tunnel** (`cloudflared`), cho phép tạo đường dẫn HTTPS công khai mà không cần cài đặt thêm phần mềm hay mở cổng mạng.

### Khởi chạy Public Web:
Chạy file batch:
```powershell
.\ux_audit_studio\run_public.bat
```
Hoặc bằng PowerShell:
```powershell
.\ux_audit_studio\run_public.ps1
```
Terminal sẽ hiển thị đường link HTTPS công khai (ví dụ: `https://xxxx.trycloudflare.com`). Bạn có thể gửi link này cho bất kỳ ai, mở trên điện thoại, máy tính bảng hoặc máy tính khác ngoài mạng nội bộ.

---

## 💻 2. Chế độ Ứng dụng Desktop Windows (.exe / Cửa sổ phần mềm độc lập)

Không cần mở qua tab trình duyệt thông thường, bạn có thể chạy ứng dụng dưới dạng một **cửa sổ phần mềm Desktop độc lập**:
- Nhấp đúp vào:
  ```
  ux_audit_studio\launch_desktop.bat
  ```
- Ứng dụng sẽ tự động bật lên trong một cửa sổ ứng dụng Windows riêng biệt (không thanh địa chỉ, không tab trình duyệt), hoạt động như một phần mềm Windows desktop chuyên nghiệp.

---

## 🏠 3. Chế độ Chạy Cục bộ (Localhost)
```powershell
.\ux_audit_studio\run_app.ps1
```
Truy cập tại: `http://localhost:8501`.
