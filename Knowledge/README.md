# 📚 Knowledge Directory

Thư mục `Knowledge/` đóng vai trò là cơ sở tri thức (Knowledge Base) trung tâm của hệ thống. Đây là nơi chứa tài liệu tham khảo, dữ liệu nền tảng, thuật ngữ chuyên ngành và tài liệu hỗ trợ cho kỹ thuật RAG (Retrieval-Augmented Generation).

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Knowledge/
├── README.md
├── domain/               # Tri thức theo lĩnh vực chuyên môn (Tài chính, Kỹ thuật, Marketing, ...)
│   ├── terminology.md    # Thuật ngữ chuyên ngành
│   └── standards.md      # Tiêu chuẩn áp dụng
├── products/             # Tài liệu chi tiết về sản phẩm/dịch vụ
│   └── user_guide.md
└── vector_index/         # Dữ liệu index vector dùng cho tìm kiếm ngữ nghĩa (RAG)
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Cung cấp ngữ cảnh rộng**: Giúp Agent đưa ra câu trả lời chuẩn xác dựa trên dữ liệu chuẩn của tổ chức/dự án thay vì suy đoán (hallucination).
2. **Nguồn tri thức dùng chung**: Tất cả các Agent và sub-agent đều có thể truy cập để tra cứu thông tin nền.

---

## 💡 Hướng Dẫn Sử Dụng Cho AI Agent

- **Tra cứu trước khi thực thi**: Trước khi đưa ra quyết định hoặc phản hồi phức tạp, Agent nên quét thư mục `Knowledge/` để tìm các tài liệu liên quan.
- **Cập nhật tri thức**: Khi phát hiện tri thức mới được kiểm chứng từ các dự án thành công, Agent đề xuất hoặc lưu tài liệu mới vào thư mục này theo cấu trúc phân loại rõ ràng.
- **Định dạng tối ưu**: Ưu tiên định dạng Markdown (`.md`) hoặc `JSON` để Agent có thể phân tích và truy xuất nhanh chóng.
