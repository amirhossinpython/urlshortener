from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # صفحه اصلی برای گرفتن لینک
    path('<str:code>/', views.redirect_link, name='redirect'),  # ریدایرکت
]
