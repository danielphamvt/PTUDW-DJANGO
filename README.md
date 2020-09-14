## Tutorial session 1: Tạo dự án Django đầu tiên:

1. Cài đặt Django: ```conda install django``` hoặc ```pip install django``` (nên cài Virtual environment)
2. ```django-admin startproject ten_website```
3. ```cd ten_website``` (Chuyển đến thư mục root làm việc chứa website)
4. ```python manage.py runserver``` (Chạy thử server lần đầu tiên)
5. ```python manage.py migrate``` (Tạo CSDL SQLite với admin, authentication, sessions ...)
6. ```python manage.py createsuperuser``` (Tạo TK quản trị cao nhất)
7. http://127.0.0.1:8000/admin (Trang quản trị người dung, nội dung)
8. Thêm file views.py (Thêm class Home view)
9. Sửa file urls.py (thêm url cho trang “home”)
10. Sửa file setting.py (templates path, static file directory)
11. Tự viết hoặc sử dụng Boostrap template, cho css, js vào thư mục static, cho html vào templates
12. Sửa file index.html bằng Jinja2 (add static đầu trang HTML)

Tham khảo thêm: https://docs.djangoproject.com/en/3.1/intro/tutorial01/

Cú pháp Jinja: https://jinja.palletsprojects.com/en/2.11.x/
