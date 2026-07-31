# 💻 Scripts Directory

Thư mục `Scripts/` chứa các kịch bản thực thi tự động (Automation Scripts) bằng các ngôn ngữ như Python, PowerShell, Bash, hoặc Node.js. Các script này giúp Agent thực hiện các thao tác kỹ thuật một cách chính xác và hiệu quả.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Scripts/
├── README.md
├── python/               # Các kịch bản xử lý dữ liệu, API, AI/ML
│   ├── fetch_data.py
│   └── parse_pdf.py
├── shell/                # Kịch bản dòng lệnh Linux/macOS
│   └── backup.sh
└── powershell/           # Kịch bản tự động hóa môi trường Windows
    └── setup_env.ps1
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Mở rộng năng lực thực thi**: Cho phép Agent tương tác trực tiếp với hệ thống tập tin, cơ sở dữ liệu và API bên ngoài.
2. **Chuẩn hóa công việc lặp lại**: Đảm bảo các tác vụ kỹ thuật được thực hiện nhất quán mà không cần viết lại mã từ đầu.

---

## ⚠️ Quy Tắc Viết Script Cho Agent

- **Tính an toàn (Safety First)**: Tất cả script phải có cơ chế kiểm tra lỗi (Try/Catch), kiểm tra đầu vào và không xóa dữ liệu nguy hiểm mà không có cảnh báo.
- **Idempotency**: Script chạy 1 lần hay 100 lần trên cùng input đều cho ra kết quả nhất quán mà không làm hỏng trạng thái hệ thống.
- **Tài liệu hóa (Docstrings)**: Mọi script phải có comment giải thích rõ: mục đích, tham số đầu vào (Inputs), và đầu ra mong đợi (Outputs).
