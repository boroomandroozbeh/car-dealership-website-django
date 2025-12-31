from django.shortcuts import render, get_object_or_404 , redirect
from core.models import Car, Article, Tag, Brand
from django.core.paginator import Paginator
from django.db.models import Q
from core.forms import ContactForm


# Create your views here.


def home(request):
    cars = Car.objects.filter(is_active=True).order_by("-created_at")[:5]
    popular_car_tags = Tag.objects.filter(tag_type="car")[:6]
    return render(request, "core/pages/home.html", {"cars": cars, "popular_car_tags": popular_car_tags})


def cars_list(request):
    brands = Brand.objects.all()

    # 1) کوئری پایه
    qs = Car.objects.filter(is_active=True)
    years = ["1404", "1403", "1402", "1401", "1400", "1399", "1398", "1397", "1395"]

    # 2) فیلترها از GET
    q = request.GET.get("q")
    brand = request.GET.get("brand")
    year_min = request.GET.get("year_min")
    year_max = request.GET.get("year_max")
    price_max = request.GET.get("price_max")
    gear = request.GET.get("gear")
    sort = request.GET.get("sort")

    if q:
        qs = qs.filter(title__icontains=q)

    if brand:
        qs = qs.filter(brand_id=brand)

    if year_min:
        qs = qs.filter(year__gte=year_min)

    if year_max:
        qs = qs.filter(year__lte=year_max)

    if price_max:
        qs = qs.filter(price__lte=price_max)

    if gear:
        qs = qs.filter(gear_type=gear)

    # 3) مرتب‌سازی
    if sort == "cheap":
        qs = qs.order_by("price")
    elif sort == "expensive":
        qs = qs.order_by("-price")
    elif sort == "low_mileage":
        qs = qs.order_by("mileage")
    else:
        # پیش‌فرض: جدیدترین‌ها
        qs = qs.order_by("-created_at")

    # 4) صفحه‌بندی
    paginator = Paginator(qs, 6)  # ۵ ماشین در هر صفحه (هر عددی که خودت خواستی)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=1,
        on_ends=1,
    )

    context = {
        "cars": page_obj,
        "page_obj": page_obj,
        "page_range": page_range,
        "brands": brands,
        "years": years,
    }
    return render(request, "core/pages/cars-list.html", context)


def car_detail(request, slug):
    car = get_object_or_404(Car, slug=slug, is_active=True)

    # خودروهای مشابه:
    # همان برند، فعال، غیر از خود این ماشین
    similar_cars = (
        Car.objects.filter(is_active=True, brand=car.brand)
        .exclude(id=car.id)  # type: ignore
        .order_by("-created_at")[:3]
    )

    context = {
        "car": car,
        "similar_cars": similar_cars,
    }
    return render(request, "core/pages/car-detail.html", context)


def aboutUs(request):
    return render(request, "core/pages/about-us.html")




def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # ذخیره در دیتابیس
            return redirect("contact_success")
    else:
        form = ContactForm()

    return render(request, "core/pages/contact-us.html", {"form": form})


def contact_success(request):
    return render(request, "core/pages/contact-success.html")



def article_detail(request, slug):
    article = get_object_or_404(
        Article,
        slug=slug,
        is_published=True,
    )

    # مقالات مشابه: همان دسته یا تگ مشترک
    similar_articles = Article.objects.filter(
        is_published=True,
        category=article.category,
    ).exclude(id=article.id).order_by("-published_at", "-created_at")[:6] # type: ignore

    context = {
        "article": article,
        "similar_articles": similar_articles,
    }
    return render(request, "core/pages/article-detail.html", context)


def exhibition_esfahan(request):
    return render(request, "core/pages/exhibition-esfahan.html")


def faq(request):
    return render(request, "core/pages/faq.html")


def cars_by_tag(request, slug):
    # فقط تگ‌های مخصوص ماشین
    tag = get_object_or_404(Tag, slug=slug, tag_type="car")

    qs = (
        Car.objects.filter(
            is_active=True,
            tags=tag,
        )
        .order_by("-created_at")
        .distinct()
    )

    paginator = Paginator(qs, 6)  # ۱۲ ماشین در هر صفحه
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=1,
        on_ends=1,
    )

    context = {
        "cars": page_obj,
        "page_obj": page_obj,
        "page_range": page_range,
        "current_tag": tag,  # برای نمایش عنوان صفحه
    }
    return render(request, "core/pages/cars-list.html", context)




def articles_list(request):
    tags = Tag.objects.filter(tag_type="article")
    qs = Article.objects.filter(is_published=True).order_by("-updated_at")

    # جستجو (اگر قبلاً اضافه کردیم)
    q = request.GET.get("q")
    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(summary__icontains=q) |
            Q(content__icontains=q)
        )

    paginator = Paginator(qs, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=1,
        on_ends=1,
    )

    context = {
        "tags": tags,
        "articles": page_obj,
        "page_obj": page_obj,
        "page_range": page_range,
        "current_tag": None,   # مهم برای active شدن دکمه‌ها
    }
    return render(request, "core/pages/articles.html", context)


def articles_by_tag(request, slug):
    tags = Tag.objects.filter(tag_type="article")
    current_tag = get_object_or_404(Tag, slug=slug, tag_type="article")

    qs = Article.objects.filter(is_published=True, tags=current_tag).order_by("-updated_at")

    # جستجو داخل همین تگ (اختیاری)
    q = request.GET.get("q")
    if q:
        qs = qs.filter(
            Q(title__icontains=q) |
            Q(summary__icontains=q) |
            Q(content__icontains=q)
        )

    paginator = Paginator(qs, 9)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    page_range = paginator.get_elided_page_range(
        number=page_obj.number,
        on_each_side=1,
        on_ends=1,
    )

    context = {
        "tags": tags,
        "articles": page_obj,
        "page_obj": page_obj,
        "page_range": page_range,
        "current_tag": current_tag,  # اینجا پر می‌کنیم
    }
    return render(request, "core/pages/articles.html", context)
