from django.db import models




class Car(models.Model):
    GEAR_CHOICES = (
        ("manual", "دنده‌ای"),
        ("auto", "اتومات"),
    )

    FUEL_CHOICES = (
        ("benzin", "بنزین"),
        ("gas", "گاز"),
        ("hybrid", "هیبرید"),
        ("diesel", "دیزل"),
    )

    title = models.CharField(max_length=200, verbose_name="عنوان آگهی")
    brand = models.ForeignKey(
        "Brand",
        on_delete=models.PROTECT,
        related_name="cars",
        verbose_name="برند",
    )
    model = models.CharField(max_length=100, verbose_name="مدل")
    year = models.PositiveIntegerField(verbose_name="سال تولید")
    mileage = models.PositiveIntegerField(verbose_name="کارکرد (کیلومتر)")


    tags = models.ManyToManyField(
        "Tag",
        blank=True,
        related_name="cars",
        verbose_name="تگ‌ها",
        limit_choices_to={"tag_type": "car"},
    )



    features = models.ManyToManyField(
        "Feature",
        blank=True,
        related_name="cars",
        verbose_name="امکانات و آپشن‌ها",
    )


    gear_type = models.CharField(
        max_length=10,
        choices=GEAR_CHOICES,
        verbose_name="نوع گیربکس",
    )
    fuel_type = models.CharField(
        max_length=10,
        choices=FUEL_CHOICES,
        default="benzin",
        verbose_name="نوع سوخت",
    )

    body_status = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="وضعیت بدنه (بدون رنگ، دو تکه رنگ و ...)",
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        verbose_name="رنگ بدنه",
    )

    price = models.BigIntegerField(
        null=True,
        blank=True,
        verbose_name="قیمت (تومان)",
    )
    city = models.CharField(max_length=100, verbose_name="شهر")

    description = models.TextField(
        blank=True,
        verbose_name="توضیحات فروشنده / توضیحات خودرو",
    )

    main_image = models.ImageField(
        upload_to="cars/",
        verbose_name="عکس اصلی خودرو",
    )

    is_active = models.BooleanField(
        default=True,
        verbose_name="نمایش در سایت",
    )
    is_featured = models.BooleanField(
        default=False,
        verbose_name="خودرو ویژه (نمایش در صفحه اصلی)",
    )


    owner_count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="تعداد مالک قبلی",
    )

    has_accident = models.BooleanField(
        default=False,
        verbose_name="سابقه تصادف",
    )

    # ✅ این سه تا رو اضافه کن:
    body_inspection_done = models.BooleanField(
        default=False,
        verbose_name="کارشناسی بدنه",
    )

    technical_inspection_done = models.BooleanField(
        default=False,
        verbose_name="کارشناسی فنی",
    )

    written_report_available = models.BooleanField(
        default=False,
        verbose_name="گزارش کتبی کارشناسی",
    )

    insurance_valid_until = models.DateField(
        blank=True,
        null=True,
        verbose_name="اعتبار بیمه",
    )


    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name="آدرس سئو (slug) برای صفحه خودرو",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )

    def body_inspection_display(self):
        if self.body_inspection_done:
            return "✔ انجام شده"
        return "✘ انجام نشده"

    def technical_inspection_display(self):
        if self.technical_inspection_done:
            return "✔ انجام شده"
        return "✘ انجام نشده"

    def written_report_display(self):
        if self.written_report_available:
            return "✔ قابل ارائه"
        return "✘ غیر قابل ارائه"

    def get_specs(self):
        return [
            ("برند", self.brand),
            ("مدل", self.model),
            ("سال تولید", self.year),
            ("کارکرد", f"{self.mileage} کیلومتر" if self.mileage else None),
            ("گیربکس", self.get_gear_type_display()),
            ("سوخت", self.get_fuel_type_display()),
            ("رنگ بدنه", self.color),
            ("وضعیت بدنه", self.body_status or None),
        ]



    class Meta:
        verbose_name = "خودرو"
        verbose_name_plural = "خودروها"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title
