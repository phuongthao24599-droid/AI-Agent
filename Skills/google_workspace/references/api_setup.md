# 🔑 Google Workspace API Setup Guide

Tài liệu hướng dẫn cấu hình **Google Cloud Project**, kích hoạt Google Workspace APIs và tạo chìa khóa truy cập cho AI Agent.

---

## 🛠️ Bước 1: Tạo Dự Án Trên Google Cloud Console

1. Truy cập [Google Cloud Console](https://console.cloud.google.com/).
2. Nhấp chọn **Select a project** > **New Project**.
3. Đặt tên dự án (Ví dụ: `AI-Agent-Workspace`) và nhấn **Create**.

---

## 🔌 Bước 2: Kích Hoạt Các API Cần Thiết

Vào menu **APIs & Services > Library**, tìm kiếm và kích hoạt 5 API sau:
- [x] **Gmail API**
- [x] **Google Calendar API**
- [x] **Google Drive API**
- [x] **Google Sheets API**
- [x] **Google Docs API**

---

## 🔒 Bước 3: Tạo Credentials (Tài Khoản Dịch Vụ - Service Account)

### Cách A: Dùng Service Account (Khuyên Dùng Cho Agent Tự Động)
1. Vào **APIs & Services > Credentials** > **Create Credentials** > **Service Account**.
2. Đặt tên Service Account (Ví dụ: `agent-gworkspace-bot`).
3. Cấp quyền Role: `Editor` hoặc `Owner`.
4. Nhấn vào Service Account vừa tạo > Chọn tab **Keys** > **Add Key** > **Create new key** (Định dạng **JSON**).
5. Tải file JSON về và lưu vào vị trí:
   `Credentials/service_account.json`

> ⚠️ **Lưu ý:** Để Service Account truy cập được Google Drive hoặc Google Sheet cá nhân, hãy nhấn nút **Share** (Chia sẻ) trên tệp đó và nhập địa chỉ Email của Service Account (dạng `...@...iam.gserviceaccount.com`).

---

### Cách B: Dùng OAuth 2.0 Client ID (Cho Tài Khoản Cá Nhân)
1. Vào **APIs & Services > OAuth consent screen**:
   - Chọn User Type: **External** (hoặc Internal nếu dùng Google Workspace Doanh nghiệp).
   - Nhập thông tin ứng dụng cơ bản.
2. Vào **Credentials > Create Credentials > OAuth client ID**:
   - Application type: **Desktop App**.
   - Nhấn **Create** và tải file `credentials.json`.
3. Lưu file vào vị trí:
   `Credentials/google_workspace_credentials.json`

---

## 📦 Cài Đặt Thư viện Python Cho Hệ Thống

Chạy lệnh sau trong PowerShell / Command Prompt:

```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
