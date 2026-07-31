# 🧠 Memory Directory

Thư mục `Memory/` duy trì trạng thái bộ nhớ của Agent qua các phiên làm việc (Cross-session Persistence). Gồm có Bộ nhớ ngắn hạn (Short-Term Memory - STM) và Bộ nhớ dài hạn (Long-Term Memory - LTM).

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Memory/
├── README.md
├── short_term/           # Ngữ cảnh phiên làm việc hiện tại, cache tạm thời
│   └── current_context.json
├── long_term/            # Bộ nhớ tích lũy lâu dài (sở thích người dùng, quy tắc cá nhân)
│   ├── user_preferences.json
│   └── facts_and_rules.json
└── entities/             # Sơ đồ quan hệ thực thể (Entity Graph / Knowledge Graph)
    └── entity_relations.json
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Duy trì ngữ cảnh liên tục**: Giúp Agent không bị "quên" thông tin giữa các lần khởi động hoặc chuyển đổi phiên chat.
2. **Cá nhân hóa cao**: Ghi nhớ thói quen, cách làm việc và phong cách phản hồi ưa thích của người dùng/tổ chức.
3. **Tiết kiệm token**: Giảm thiểu việc phải gửi lại các câu lệnh nhắc (prompts) lặp đi lặp lại.

---

## 🛠️ Quy Tắc Quản Lý Bộ Nhớ Cho Agent

- **Short-Term Memory (STM)**: Được cập nhật liên tục trong quá trình thực thi task và có thể xóa bớt sau khi hoàn thành task.
- **Long-Term Memory (LTM)**: Chỉ lưu các thông tin quan trọng đã được kiểm chứng (ví dụ: "Người dùng ưu tiên dùng Tiếng Việt", "Mã nguồn dự án X dùng Python 3.11").
- **Kiểm tra trước khi trả lời**: Agent đọc `Memory/` để đảm bảo phong cách và ngữ cảnh nhất quán.
