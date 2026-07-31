# 🔑 Credentials Directory

Thư mục `Credentials/` là nơi quản lý tập trung các thông tin xác thực, khóa API (API Keys), Token, chứng chỉ bảo mật và file cấu hình môi trường cho hệ thống AI Agent.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Credentials/
├── README.md
├── .env.example          # File mẫu các biến môi trường (không chứa secret thật)
├── .env.local            # File chứa các chìa khóa thực tế (đã đưa vào .gitignore)
└── keys/
    ├── service_account.json.template
    └── README.md
```

---

## 🔒 Quy Tắc Bảo Mật Tuyệt Đối (Strict Security Rules)

> [!CAUTION]
> **CẢNH BÁO BẢO MẬT HÀNG ĐẦU**
> - **KHÔNG BAO GIỜ** commit các secret thật, API key, mật khẩu lên Git repository.
> - Luôn thêm các file cấu hình chứa secret vào `.gitignore`.

1. **File Mẫu (.example)**: Mọi cấu hình cần chìa khóa phải có file template đính kèm (ví dụ `.env.example`) để chỉ rõ các biến môi trường cần thiết.
2. **Truy cập an toàn**: Agent chỉ đọc các chìa khóa khi cần thực hiện các tác vụ tích hợp hệ thống ngoài (như OpenAI API, Google Cloud, Database, Webhook).
3. **Mã hóa nếu cần**: Các chứng chỉ hoặc file key quan trọng cần được lưu trữ ở dạng mã hóa hoặc thông qua Trình quản lý Secret (Secret Manager).

---

## 🛠️ Cách AI Agent Sử Dụng Thư Mục Này

- Khi kết nối dịch vụ external, Agent sẽ kiểm tra biến môi trường hoặc đọc file cấu hình trong `Credentials/`.
- Nếu thiếu chìa khóa, Agent phải ghi log lỗi vào `Logs/` và báo cáo thiếu credential chứ không tự tạo key giả lập.
