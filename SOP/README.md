# 📋 SOP (Standard Operating Procedures) Directory

Thư mục `SOP/` chứa các Quy trình vận hành chuẩn (Standard Operating Procedures). Đây là tập hợp các tài liệu hướng dẫn từng bước (Step-by-step Guides) để Agent thực hiện các công việc phức tạp theo đúng tiêu chuẩn của tổ chức.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
SOP/
├── README.md
├── client_onboarding.md   # Quy trình tiếp nhận khách hàng mới
├── code_review_sop.md     # Quy trình kiểm tra & duyệt mã nguồn
├── incident_response.md   # Quy trình xử lý sự cố hệ thống
└── report_generation.md   # Quy trình thu thập số liệu & tạo báo cáo
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Đảm bảo chất lượng đồng đều**: Giúp Agent thực hiện tác vụ theo đúng trình tự chuẩn, không bỏ sót bước quan trọng nào.
2. **Giảm thiểu sai sót**: Đưa ra các mốc kiểm tra (Checklists) và điều kiện rẽ nhánh rõ ràng khi gặp tình huống bất ngờ.

---

## 📄 Cấu Trúc Chuẩn Của File SOP

Mỗi file SOP trong thư mục nên tuân thủ bố cục:
1. **Mục đích & Phạm vi áp dụng**
2. **Điều kiện tiên quyết (Prerequisites)**
3. **Quy trình chi tiết từng bước (Step 1, Step 2, ...)**
4. **Tiêu chuẩn nghiệm thu (Acceptance Criteria)**
5. **Kế hoạch dự phòng khi có lỗi (Fallback Procedure)**

---

## ⚠️ Quy Tắc Bắt Buộc Đối Với AI Agent

- Nếu một nhiệm vụ trong `Tasks/` khớp với một SOP trong thư mục này, Agent **bắt buộc** phải tuân thủ đúng trình tự được ghi trong SOP đó.
- Không tự ý bỏ qua các bước kiểm tra chất lượng (Quality Checkpoints).
