# 🎯 Tasks Directory

Thư mục `Tasks/` là trung tâm điều phối công việc của hệ thống AI Agent. Nơi đây quản lý danh sách yêu cầu, theo dõi tiến độ, và lưu trữ trạng thái thực thi của từng nhiệm vụ.

---

## 📁 Cấu Trúc Thư Mục Gợi Ý

```
Tasks/
├── README.md
├── backlog/              # Các công việc chờ xử lý trong tương lai
│   └── TASK-003_upgrade_deps.md
├── todo/                 # Các nhiệm vụ chuẩn bị thực thi
│   └── TASK-001_analyze_market.md
├── in_progress/          # Nhiệm vụ đang được Agent xử lý
│   └── TASK-002_create_landing.md
└── completed/            # Nhiệm vụ đã hoàn tất & nghiệm thu
    └── TASK-000_setup_system.md
```

---

## 🎯 Ý Nghĩa & Mục Đích

1. **Quản lý vòng đời nhiệm vụ (Task Lifecycle)**: Theo dõi rõ ràng trạng thái công việc từ lúc tạo ra đến khi hoàn thành.
2. **Phân chia nhiệm vụ cho Agent**: Giúp Agent biết mình cần làm gì tiếp theo mà không bị trùng lặp công việc với Agent khác.

---

## 📋 Đăng Ký Yêu Cầu Nhiệm Vụ (Task Format)

Mỗi file Task cần chứa các thông tin sau:
- **Task ID & Title**: Mã định danh (ví dụ `TASK-001`) và Tiêu đề
- **Assignee**: Agent chịu trách nhiệm
- **Priority**: Mức độ ưu tiên (High, Medium, Low)
- **Description**: Mô tả chi tiết yêu cầu
- **Acceptance Criteria**: Tiêu chí đánh giá hoàn thành

---

## 🔄 Trình Tự Chuyển Trạng Thái (Task Workflow)

```
[backlog] ──> [todo] ──> [in_progress] ──> [completed]
```

1. Agent nhận task từ `todo/` và di chuyển file sang `in_progress/`.
2. Thực thi công việc theo `SOP/` và `Skills/`.
3. Sau khi tạo báo cáo trong `Reports/` và ghi log trong `Logs/`, di chuyển file task sang `completed/`.
