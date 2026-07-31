# 🏢 Clients Directory

Thư mục `Clients/` chịu trách nhiệm lưu trữ và quản lý toàn bộ thông tin hồ sơ, cấu hình riêng, yêu cầu đặc thù và lịch sử tương tác của từng khách hàng hoặc đối tác.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Clients/
├── README.md
├── client_alpha/
│   ├── profile.json       # Thông tin tổng quan (tên, liên hệ, gói dịch vụ)
│   ├── requirements.md    # Yêu cầu chi tiết & phạm vi công việc của khách hàng
│   └── history.md         # Lịch sử tương tác và ghi chú đặc thù
└── client_beta/
    ├── profile.json
    └── requirements.md
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Cá nhân hóa trải nghiệm**: Giúp Agent hiểu rõ bối cảnh, văn phong, và yêu cầu riêng biệt của từng khách hàng.
2. **Quản lý dữ liệu tách biệt**: Đảm bảo thông tin giữa các đối tác/khách hàng không bị lẫn lộn.
3. **Theo dõi tiến độ theo đối tượng**: Dễ dàng tra cứu các ưu tiên và thỏa thuận dịch vụ (SLA).

---

## ⚠️ Quy Tắc Dành Cho AI Agent

- **Quyền riêng tư (Data Privacy)**: Không trộn lẫn hoặc chia sẻ thông tin giữa các thư mục khách hàng khác nhau.
- **Định dạng dữ liệu**: Ưu tiên lưu thông tin tổng quan ở dạng cấu trúc (`JSON` hoặc `YAML`) và ghi chú chi tiết ở dạng `Markdown`.
- **Cập nhật thông tin**: Khi có thay đổi từ phía khách hàng (được xác nhận trong meeting hoặc task), Agent cần cập nhật vào file `profile.json` hoặc `history.md` tương ứng.
