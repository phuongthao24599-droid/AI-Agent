# 🏗️ Projects Directory

Thư mục `Projects/` chứa các dự án cụ thể mà Agent đang xây dựng, bảo trì hoặc tham gia phát triển. Đây là không gian lưu trữ mã nguồn (Source Code), file thiết kế và sản phẩm bàn giao (Deliverables).

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Projects/
├── README.md
├── project_website_v2/   # Thư mục cho Dự án A
│   ├── src/
│   ├── docs/
│   └── project_manifest.json
└── project_analytics_tool/ # Thư mục cho Dự án B
    ├── scripts/
    └── README.md
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Quản lý sản phẩm thực tế**: Chứa kết quả trực tiếp của các công việc phát triển (Codebase, Web App, Data Pipeline...).
2. **Cách ly từng dự án**: Đảm bảo các dự án độc lập không gây xung đột dependency hoặc cấu hình.

---

## ⚠️ Quy Tắc Quản Lý Dành Cho Agent

- **Project Manifest**: Mỗi project nên có 1 file cấu hình hoặc `README.md` riêng giải thích cách build, run, và test.
- **Tuân thủ tiêu chuẩn mã nguồn**: Mã nguồn được sinh ra phải theo chuẩn clean code, có comment rõ ràng và tuân thủ kiến trúc đã định nghĩa trong `Knowledge/` hoặc `SOP/`.
- **Kiểm thử tự động**: Dự án trong thư mục này cần kèm theo kịch bản test để Agent kiểm tra trước khi xác nhận hoàn tất.
