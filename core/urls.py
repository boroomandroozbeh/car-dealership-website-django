from django.urls import path
from . import views


urlpatterns = [
    # صفحه اصلی
    path("", views.home, name="home"),

    # لیست خودروها
    path("خرید-خودرو/", views.cars_list, name="cars_list"),

    # جزئیات خودرو – بعداً بر اساس slug داینامیکش می‌کنیم
    path("خودرو/<slug:slug>/", views.car_detail, name="car_detail"),

    # درباره ما
    path("درباره-دنیا-خودرو/", views.aboutUs, name="about-us"),

    # تماس با ما
    path("تماس/", views.contact, name="contact"),

    path("تماس/موفق/", views.contact_success, name="contact_success"),

    # لیست مقالات
    path("اخبار-خودرو/", views.articles_list, name="articles_list"),


    path("اخبار-خودرو/تگ/<slug:slug>/", views.articles_by_tag, name="articles_by_tag"),


    # صفحه جزئیات هر مقاله
    path("اخبار/<slug:slug>/", views.article_detail, name="article_detail"),

    # نمایشگاه ماشین اصفهان
    path("نمایشگاه-ماشین-اصفهان/", views.exhibition_esfahan, name="exhibition_esfahan"),

    # سوالات متداول
    path("سوالات-متداول/", views.faq, name="faq"),


    path("خودرو/تگ/<slug:slug>/", views.cars_by_tag, name="cars_by_tag"),

]