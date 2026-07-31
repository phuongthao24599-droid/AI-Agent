# 📜 Logs Directory

Thư mục `Logs/` lưu trữ toàn bộ nhật ký hoạt động (Activity Logs), vết suy luận (Reasoning Trace), thông tin lỗi (Error Logs) và lịch sử thực thi của Agent trong hệ thống.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Logs/
├── README.md
├── daily/                # Log hoạt động theo ngày (ví dụ: 2026-07-31.log)
├── execution/            # Log thực thi chi tiết của các kịch bản trong Scripts/
└── errors/               # Log tập trung các sự cố và ngoại lệ (exceptions)
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Audit & Giám sát**: Giúp con người và hệ thống theo dõi minh bạch các bước Agent đã thực hiện.
2. **Khắc phục lỗi (Debugging)**: Truy vết nguyên nhân gốc rễ khi kịch bản hoặc task thất bại.
3. **Đánh giá hiệu năng**: Phân tích thời gian phản hồi, số token tiêu thụ, và độ hiệu quả của từng Agent.

---

## 📋 Đơn Vị & Định Dạng Log Chuẩn

Mỗi dòng log nên tuân theo định dạng chuẩn (JSON Lines hoặc Text có Timestamp ISO 8601):

```json
{"timestamp": "2026-07-31T09:18:15Z", "agent_id": "main_agent", "level": "INFO", "task_id": "TASK-001", "message": "Successfully executed script parse_data.py"}
```

---

## ⚠️ Quy Tắc Dành Cho AI Agent

- **Ghi log tự động**: Mỗi khi hoàn thành bước quan trọng hoặc gặp sự cố, Agent bắt buộc ghi log vào thư mục này.
- **Không ghi đè dữ liệu lịch sử**: Luôn dùng chế độ ghi nối (Append mode).
- **Dọn dẹp định kỳ**: Áp dụng quy tắc xoay vòng log (Log rotation) nếu file quá lớn.
