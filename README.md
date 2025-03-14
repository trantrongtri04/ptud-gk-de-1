# Django Blog Project

## Giới thiệu

Dự án này là một ứng dụng Blog được xây dựng bằng framework Django. Blog hỗ trợ các tính năng quản lý bài viết, người dùng và dashboard thống kê thông tin cơ bản.

## Cấu trúc thư mục dự án

```
MYBLOG/
├── myblog/                    # Thư mục cấu hình chính của dự án
├── posts/                     # Ứng dụng quản lý bài viết
├── users/                     # Ứng dụng quản lý người dùng
├── static/                    # Thư mục chứa file tĩnh (CSS, JS, images)
├── templates/                 # Thư mục chứa các file template
│     ├── base.html            # Template chung cho cả dự án
│     ├── blog/
│     └── users/
├── db.sqlite3                 # Cơ sở dữ liệu SQLite mặc định
├── manage.py                  # File quản lý dự án Django
└── requirements.txt           # Thư viện cần thiết để chạy dự án
```

## Cài đặt và chạy dự án

### Bước 1: Clone dự án

```bash
git clone https://github.com/trantrongtri04/ptud-gk-de-1.git
```

### Bước 2: Di chuyển vào thư mục dự án
```bash
cd ptud-gk-de-1
```

### Bước 3: Tạo và kích hoạt môi trường ảo

```bash
python -m venv env

# Windows
.\venv\Scripts\activate

# macOS/Linux
source env/bin/activate
```

### Bước 4: Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

### Bước 5: Chạy migrations để tạo database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Bước 6: Tạo tài khoản admin (tùy chọn)

```bash
python manage.py createsuperuser
```

### Bước 7: Chạy server

```bash
python manage.py runserver
```

Mở trình duyệt và truy cập `http://127.0.0.1:8000/`

## Các tính năng chính

- Quản lý bài viết (thêm, sửa, xóa, xem chi tiết)
- Đăng nhập, đăng ký và quản lý người dùng
- Dashboard thống kê tổng số bài viết và danh sách bài viết gần đây