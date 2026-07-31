# 🛠️ Skills Directory

Thư mục `Skills/` quản lý danh mục các kỹ năng (Tool Definition / Agent Skills) dạng mô-đun hóa. Kỹ năng định nghĩa xem Agent "biết làm gì" và "làm như thế nào" thông qua các bộ công cụ được đăng ký.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Skills/
├── README.md
├── web_search/           # Kỹ năng tìm kiếm web & tổng hợp
│   ├── SKILL.md          # Định nghĩa kỹ năng, hướng dẫn prompt & tham số
│   └── helper.py
├── data_analysis/        # Kỹ năng phân tích số liệu
│   ├── SKILL.md
│   └── chart_generator.py
└── pdf_parser/           # Kỹ năng đọc & trích xuất PDF
    └── SKILL.md
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Mô-đun hóa năng lực (Modularity)**: Tách biệt các khả năng của Agent thành các bộ kỹ năng độc lập, dễ dàng bật/tắt hoặc nâng cấp.
2. **Chuẩn giao tiếp (Schema)**: Quy định định dạng Input/Output chính xác để Agent biết cách gọi công cụ mà không bị nhầm lẫn tham số.

---

## 📋 Đăng Ký Kỹ Năng Mới (`SKILL.md`)

File `SKILL.md` trong mỗi thư mục kỹ năng cần khai báo:
- **Name**: Tên kỹ năng (duy nhất)
- **Description**: Mô tả ngắn gọn khi nào nên dùng kỹ năng này
- **Parameters**: Danh sách các tham số truyền vào
- **Usage Example**: Ví dụ lệnh gọi hoặc prompt mẫu

---

## 🛠️ Hướng Dẫn Dành Cho Agent

- Khi nhận Task, Agent quét thư mục `Skills/` để đối chiếu xem mình đã có sẵn kỹ năng phù hợp hay chưa trước khi tiến hành thực hiện.
