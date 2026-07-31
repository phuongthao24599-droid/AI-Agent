# 📊 Reports Directory

Thư mục `Reports/` là nơi chứa các báo cáo đầu ra (Outputs), tổng kết công việc, phân tích dữ liệu, và kết quả đánh giá do AI Agent biên soạn.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Reports/
├── README.md
├── daily/                # Báo cáo tiến độ hàng ngày
│   └── 2026-07-31_daily_report.md
├── task_outputs/         # Kết quả báo cáo theo từng Task cụ thể
│   └── TASK-001_market_analysis.md
└── summary/              # Báo cáo tổng hợp tuần/tháng hoặc dự án
    └── 2026-Q3_performance_summary.md
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Bàn giao kết quả (Deliverables)**: Nơi người dùng và quản lý truy cập để xem kết quả công việc mà Agent đã thực hiện.
2. **Minh chứng hoàn thành**: Cung cấp số liệu, biểu đồ, kết quả phân tích cụ thể để chứng minh task đã được hoàn thành đúng chất lượng.

---

## 📋 Định Dạng Chuẩn Của Một Báo Cáo

Một file báo cáo trong `Reports/` nên có các phần chính:
1. **Tiêu đề & Mục tiêu báo cáo**
2. **Tóm tắt dành cho quản lý (Executive Summary)**
3. **Chi tiết kết quả / Phân tích dữ liệu**
4. **Các khuyến nghị & Bước tiếp theo (Recommendations & Next Steps)**
5. **Phụ lục / Dữ liệu tham chiếu (nếu có)**

---

## 🛠️ Hướng Dẫn Dành Cho Agent

- Xuất báo cáo dưới dạng Markdown (`.md`), HTML hoặc JSON tùy thuộc vào yêu cầu công việc.
- Đảm bảo tính trung thực của số liệu, không tự tạo dữ liệu giả lập trừ khi được yêu cầu thử nghiệm.
