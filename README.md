# 🔗 URL Shortener Web App

یک اپلیکیشن وب حرفه‌ای برای کوتاه کردن لینک‌ها با **Django** و **HTML/CSS/JS**.  

این پروژه قابلیت:  
- کوتاه کردن لینک‌ها به آدرس‌های کوتاه و منحصر به فرد  
- شمارش تعداد کلیک‌ها روی لینک‌ها  
- 

---

## ⚙️ ویژگی‌ها

- تولید خودکار **کد کوتاه** برای هر لینک  
- ذخیره لینک‌ها و تعداد کلیک‌ها در **دیتابیس SQLite**  
- رابط کاربری ساده و زیبا با **HTML/CSS/JS**  
- ریدایرکت خودکار به لینک اصلی هنگام کلیک روی لینک کوتاه  

---

## 📂 ساختار پروژه

## 📂 ساختار پروژه

urlshortener/
├── manage.py
├── urlshortener/ # تنظیمات پروژه
│ ├── settings.py
│ └── urls.py
├── shortener/ # اپ لینک‌ها
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ ├── templates/
│ └── static/
├── requirements.txt # پکیج‌های مورد نیاز
└── .gitignore


## 🛠️ پیش‌نیازها

- Python 3.10+  
- Django 4.x  
- pip  

---

## 💻 نصب و اجرای پروژه

1. کلون کردن پروژه:

```bash
git clone https://github.com/amirhossinpython/urlshortener.git
cd urlshortener

## 🛠️ نصب و اجرای پروژه

### ۱. ساخت محیط مجازی
```bash
python -m venv venv

فعال کردن محیط مجازی
ویندوز :
venv\Scripts\activate

لینوکس/مک:
source venv/bin/activate


نصب پکیج‌های نیاز شما :
pip install -r requirements.txt
اعمال دیتابیس :
python manage.py makemigrations
python manage.py migrate

اجرای سرور
python manage.py runserver

