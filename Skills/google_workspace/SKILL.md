# 🛠️ Google Workspace Skill Guide

Kỹ năng **Google Workspace** giúp AI Agent tương tác trực tiếp với các dịch vụ đám mây của Google gồm **Gmail, Google Calendar, Google Drive, Google Sheets, và Google Docs**.

---

## 📐 Cấu Trúc Mô-đun Kỹ Năng

```
Skills/google_workspace/
├── SKILL.md                  # Hướng dẫn chi tiết kỹ năng (File này)
├── scripts/
│   └── gworkspace_client.py   # Script thực thi mã nguồn Python chính
└── references/
    └── api_setup.md          # Hướng dẫn cấu hình Google Cloud Console & API Scope
```

---

## 🎯 Chi Tiết Khả Năng & Công Cụ (Capabilities)

### 1. 📧 Gmail Management
- **Gửi Email (`gmail send`)**: Gửi email định dạng HTML hoặc Plain Text kèm theo file đính kèm.
- **Tìm kiếm Email (`gmail search`)**: Tra cứu thư theo từ khóa, sender, ngày gửi, nhãn (label).
- **Đọc Thư (`gmail read`)**: Trích xuất tiêu đề, người gửi, thời gian và nội dung chi tiết.
- **Tạo Thư Nháp (`gmail draft`)**: Chuẩn bị bản nháp trước khi gửi chính thức.

### 2. 📅 Google Calendar Management
- **Tạo Sự Kiện (`calendar create`)**: Thêm lịch hẹn, cuộc họp kèm đường link Google Meet, mô tả, địa điểm.
- **Xem Lịch Rảnh/Bận (`calendar list`)**: Liệt kê các sự kiện trong khoảng thời gian cụ thể.
- **Cập nhật & Hủy Lịch (`calendar update / delete`)**: Chỉnh sửa thời gian hoặc xóa sự kiện.

### 3. 📁 Google Drive Management
- **Tìm kiếm File/Folder (`drive search`)**: Tra cứu theo tên, loại file (MIME type) hoặc thư mục cha.
- **Tải Lên / Tải Về (`drive upload / download`)**: Đồng bộ dữ liệu giữa máy cục bộ và Google Drive.
- **Tạo Thư Mục (`drive create-folder`)**: Quản lý cây thư mục lưu trữ.
- **Phân Quyền (`drive share`)**: Chia sẻ quyền Xem (Reader), Chỉnh sửa (Editor) cho email chỉ định.

### 4. 📊 Google Sheets Management
- **Đọc Bảng Tính (`sheets read`)**: Trích xuất dữ liệu từ Sheet ID và khoảng ô (Range: `Sheet1!A1:D10`).
- **Ghi Nối Dòng (`sheets append`)**: Thêm các dòng mới vào cuối bảng tính (dùng cho ghi log, thu lead, hóa đơn).
- **Cập Nhật Ô (`sheets update`)**: Ghi đè dữ liệu vào vị trí ô xác định.
- **Tạo Trang Tính Mới (`sheets create`)**: Khởi tạo bảng tính mới trên Drive.

### 5. 📝 Google Docs Management
- **Tạo Tài Liệu (`docs create`)**: Tạo văn bản mới với tiêu đề và nội dung ban đầu.
- **Đọc Văn Bản (`docs read`)**: Lấy toàn bộ văn bản từ Doc ID.
- **Chèn Đoạn Văn (`docs append`)**: Thêm nội dung, đoạn văn bản mới vào tài liệu có sẵn.

---

## 🔒 Quy Trình Xác Thực (Authentication Flow)

Dịch vụ hỗ trợ 2 phương thức xác thực chính qua thư viện `google-auth`:

1. **OAuth 2.0 (User Delegation - Dành cho tài khoản cá nhân)**:
   - Cần file `Credentials/google_workspace_credentials.json` (Client Secret).
   - Tạo file `token.json` khi ủy quyền lần đầu.
2. **Service Account (Dành cho tài khoản doanh nghiệp / Bot tự động)**:
   - Cần file `Credentials/service_account.json`.
   - Phù hợp chạy tự động 24/7 không cần giao diện đăng nhập.

---

## 📝 Mã Mẫu Thực Thi Python

Ví dụ Agent gọi hàm từ script [gworkspace_client.py](file:///c:/Users/TamDuc/Desktop/AI%20Agent/Skills/google_workspace/scripts/gworkspace_client.py):

```python
from Skills.google_workspace.scripts.gworkspace_client import GoogleWorkspaceClient

# Khởi tạo client
client = GoogleWorkspaceClient()

# 1. Gửi Mail
client.send_email(to="client@example.com", subject="Báo cáo tiến độ", body="Dạ meow, em gửi báo cáo ạ!")

# 2. Tạo cuộc họp Google Calendar
client.create_calendar_event(
    summary="Họp Tổng Kết Chiến Dịch",
    start_time="2026-08-05T09:00:00+07:00",
    end_time="2026-08-05T10:30:00+07:00",
    attendees=["sunnie@example.com"]
)

# 3. Ghi dữ liệu vào Google Sheets
client.append_sheet_row(
    spreadsheet_id="1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
    range_name="Sheet1!A1",
    values=[["2026-07-31", "Hoàn thành Task", "Sunnie"]]
)
```
