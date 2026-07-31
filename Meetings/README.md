# 🤝 Meetings Directory

Thư mục `Meetings/` lưu trữ thông tin, ghi chú, bản ghi âm/transcript, tổng hợp kết quả (Summaries) và các hành động cần thực hiện (Action Items) từ các cuộc họp nội bộ hoặc họp với khách hàng.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Meetings/
├── README.md
├── templates/
│   └── meeting_notes_template.md  # Template chuẩn cho ghi chú cuộc họp
└── 2026/
    └── 2026-07-31_kickoff_client_alpha/
        ├── raw_transcript.txt      # Bản ghi lời nói thô (nếu có)
        ├── summary.md              # Tóm tắt nội dung chính & quyết định
        └── action_items.md         # Các công việc cần làm sau cuộc họp
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Bảo toàn thông tin cuộc họp**: Chuyển đổi dữ liệu trao đổi trong cuộc họp thành tri thức có thể tra cứu.
2. **Tự động hóa phân công**: Trích xuất các Action Items để chuyển thành công việc trong thư mục `Tasks/`.
3. **Theo dõi cam kết**: Đảm bảo các thỏa thuận trong cuộc họp được Agent và team thực thi chính xác.

---

## 📋 Mẫu Báo Cáo Cuộc Họp (Meeting Summary Format)

File `summary.md` nên chứa các mục:
- **Thời gian & Thành phần tham dự**
- **Mục tiêu cuộc họp**
- **Nội dung thảo luận chính**
- **Quyết định đã thống nhất**
- **Danh sách Action Items (Giao cho ai, thời hạn)**

---

## 🛠️ Hướng Dẫn Dành Cho Agent

- Sau khi kết thúc hoặc nhận dữ liệu cuộc họp, Agent tiến hành phân tích transcript -> tạo file `summary.md` -> tự động cập nhật hoặc tạo task mới vào `Tasks/`.
