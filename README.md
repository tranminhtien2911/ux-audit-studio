# 🎨 UX Audit Studio (Pro Edition)

Ứng dụng kiểm toán và phản biện trải nghiệm người dùng (UX/UI Usability Audit) cho các luồng giao diện (UI Flow), vận dụng triệt để hệ thống tri thức và nguyên lý thiết kế từ NotebookLM:
- **Don Norman:** *The Design of Everyday Things* (Tính trực quan, Phản hồi, Affordance, Signifiers, Khoảng cách Thực thi & Đánh giá).
- **Steve Krug:** *Don't Make Me Think* (Định luật tối cao, Tính tự giải thích, Gợi ý clickability, Điều hướng "You are here").
- **Creative Tim:** *Fundamentals of Creating a Great UI/UX*.

---

## ☁️ 1. Hướng Dẫn Đưa Lên Cloud Chạy 24/7 Vĩnh Viễn (Miễn Phí 100%)

Nền tảng tối ưu nhất cho ứng dụng Streamlit là **Streamlit Community Cloud (do Snowflake tài trợ)**:
- **Chi phí:** Hoàn toàn miễn phí 24/7 vĩnh viễn.
- **Tên miền:** Sở hữu link cố định dạng `https://<ten-ban-chon>.streamlit.app`.
- **Bảo mật:** Tự động có chứng chỉ bảo mật HTTPS/SSL.
- **Tự động hóa:** Bất cứ khi nào bạn cập nhật code lên GitHub, web Cloud sẽ tự động cập nhật lại trong 60 giây.

### Bước 1: Tạo Repository trên GitHub
1. Đăng nhập vào [github.com/new](https://github.com/new).
2. Đặt tên Repository: `ux-audit-studio`.
3. Chọn chế độ: **Public**.
4. **Không cần** tích vào *"Add a README file"* (vì dự án đã có sẵn code).
5. Bấm **"Create repository"** và copy link repo (ví dụ: `https://github.com/tmtien2911/ux-audit-studio.git`).

### Bước 2: Đẩy toàn bộ mã nguồn lên GitHub (1-Click)
Chỉ cần nhấp đúp vào file:
```
ux_audit_studio\deploy_to_github.bat
```
*(Hoặc chạy `powershell -File .\ux_audit_studio\deploy_to_github.ps1`)*.
Dán link GitHub repo bạn vừa copy ở Bước 1 vào terminal và nhấn Enter. Toàn bộ mã nguồn sẽ tự động được đồng bộ lên GitHub.

### Bước 3: Kích hoạt trên Streamlit Cloud
1. Truy cập [share.streamlit.io](https://share.streamlit.io) và đăng nhập bằng tài khoản **GitHub**.
2. Bấm nút **"Create app"** (hoặc "New app") -> chọn **"Deploy a public app from GitHub"**.
3. Điền thông tin:
   - **Repository:** `tmtien2911/ux-audit-studio`
   - **Branch:** `main`
   - **Main file path:** `app.py`
   - **App URL:** Bạn có thể tự chọn tên miền phụ đẹp, ví dụ: `ux-audit-studio` (Link sẽ là: `https://ux-audit-studio.streamlit.app`).
4. Bấm vào **"Advanced settings..."** -> Mục **"Secrets"**:
   Dán cấu hình API Key:
   ```toml
   GEMINI_API_KEY = "AIzaSy..."
   
   # Tùy chọn (Nếu muốn đồng bộ trực tiếp với Notebook 'The Design of Everyday Creative Things' trên Cloud):
   # NOTEBOOKLM_COOKIES = "SID=...; HSID=...; SSID=..."
   ```
5. Bấm **"Deploy!"**.

Sau 1 - 2 phút, ứng dụng của bạn sẽ chính thức trực tuyến 24/7 vĩnh viễn trên toàn thế giới!

---

## 🌐 2. Chế Độ Chia Sẻ Tạm Thời (Cloudflare Tunnel)
Nếu bạn chỉ muốn chia sẻ link nhanh cho đồng nghiệp mà không cần đưa lên GitHub:
- Chạy: `.\ux_audit_studio\run_public.bat`
- Hệ thống sẽ tạo một link ngẫu nhiên bảo mật dạng `https://xxxx.trycloudflare.com` kết nối trực tiếp đến máy tính của bạn.

---

## 💻 3. Chế Độ Ứng Dụng Desktop Windows (.exe / Cửa Sổ Độc Lập)
Nếu muốn dùng như một phần mềm máy tính chuyên nghiệp:
- Nhấp đúp vào: `ux_audit_studio\launch_desktop.bat`
- Ứng dụng mở trong một cửa sổ ứng dụng Windows độc lập (không thanh địa chỉ, không tab trình duyệt).

---

## 🏠 4. Chế Độ Chạy Cục Bộ (Localhost)
```powershell
.\ux_audit_studio\run_app.ps1
```
Truy cập tại: `http://localhost:8501`.
