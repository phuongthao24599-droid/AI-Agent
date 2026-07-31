---
name: google_workspace
description: Kỹ năng quản lý các dịch vụ Google Workspace bao gồm Gmail (email), Google Calendar (lịch họp), Google Drive (tệp tin), Google Sheets (bảng tính), và Google Docs (tài liệu văn bản). Sử dụng khi cần gửi/đọc mail, tạo lịch hẹn, tải/up file, đọc/ghi sheet hoặc soạn thảo doc.
---

# 🌐 Google Workspace Management Skill

Kỹ năng này cung cấp khả năng tự động hóa và quản lý các dịch vụ tích hợp thuộc hệ sinh thái **Google Workspace** dành cho AI Agent.

---

## 🧰 Các Dịch Vụ Hỗ Trợ (Supported Services)

1. 📧 **Gmail**: Gửi email, tìm kiếm hộp thư, đọc thư, tạo bản nháp, quản lý nhãn.
2. 📅 **Google Calendar**: Tạo cuộc họp, tra cứu lịch rảnh/bận, cập nhật hoặc hủy sự kiện.
3. 📁 **Google Drive**: Tìm kiếm file/thư mục, tải tệp lên/xuống, phân quyền chia sẻ.
4. 📊 **Google Sheets**: Đọc dữ liệu vùng cell, thêm dòng mới (append), cập nhật ô (update), tạo bảng tính mới.
5. 📝 **Google Docs**: Tạo tài liệu mới, đọc nội dung tài liệu, chèn văn bản và định dạng cơ bản.

---

## 🔐 Xác Thực & Chìa Khóa Truy Cập (Authentication)

Kỹ năng này sử dụng bộ thư viện chính thức `google-api-python-client` và `google-auth`.

* **Vị trí Credential mẫu**: [google_workspace_credentials.json.template](file:///c:/Users/TamDuc/Desktop/AI%20Agent/Credentials/google_workspace_credentials.json.template)
* **Vị trí Credential thực tế**: `Credentials/google_workspace_credentials.json` hoặc `Credentials/service_account.json` (được bảo vệ trong `.gitignore`).

---

## 🚀 Cách Sử Dụng Qua Script Kịch Bản (CLI Commands)

Agent có thể thực thi kịch bản bằng Python tại [gworkspace_client.py](file:///c:/Users/TamDuc/Desktop/AI%20Agent/Skills/google_workspace/scripts/gworkspace_client.py):

```bash
# 📧 Gmail: Gửi email
python Skills/google_workspace/scripts/gworkspace_client.py gmail send --to "user@example.com" --subject "Tiêu đề" --body "Nội dung"

# 📅 Calendar: Tạo lịch họp
python Skills/google_workspace/scripts/gworkspace_client.py calendar create --summary "Họp Team" --start "2026-08-01T10:00:00+07:00" --end "2026-08-01T11:00:00+07:00"

# 📁 Drive: Tìm kiếm file
python Skills/google_workspace/scripts/gworkspace_client.py drive search --query "name contains 'Back to school'"

# 📊 Sheets: Ghi dữ liệu vào Bảng tính
python Skills/google_workspace/scripts/gworkspace_client.py sheets append --spreadsheet-id "ID_SHEET" --range "Sheet1!A1" --values "[['Ngày', 'Doanh thu'], ['2026-08-01', '10000000']]"

# 📝 Docs: Tạo tài liệu văn bản mới
python Skills/google_workspace/scripts/gworkspace_client.py docs create --title "Biên bản cuộc họp" --content "Nội dung cuộc họp..."
```

---

## 🛡️ Nguyên Tắc An Toàn & Bảo Mật
1. Kiểm tra kĩ thông tin người nhận trước khi gửi Email hoặc chia sẻ Drive public.
2. Tất cả hành động gửi mail/xóa file/sửa lịch phải được ghi vết vào thư mục `Logs/`.
3. Khi thiếu credential, báo lỗi rõ ràng và tuyệt đối không tạo dữ liệu giả lập.
