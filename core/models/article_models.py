from django.db import models
import math







class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان")
    slug = models.SlugField(
        max_length=220,
        unique=True,
        verbose_name="آدرس سئو (slug)",
    )

    image = models.ImageField(
        upload_to="articles/",
        null=True,
        blank=True,
        verbose_name="تصویر مقاله",
    )

    # 🆕 دسته‌بندی
    category = models.ForeignKey(
        "core.Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="articles",
        verbose_name="دسته‌بندی",
    )

    # 🆕 تگ‌ها
    tags = models.ManyToManyField(
        "core.Tag",
        blank=True,
        related_name="articles",
        verbose_name="تگ‌ها",
        limit_choices_to={"tag_type": "article"},
    )


    summary = models.TextField(
        blank=True,
        verbose_name="خلاصه کوتاه (متن لیست)",
    )
    content = models.TextField(verbose_name="متن کامل مقاله")


    is_published = models.BooleanField(
        default=True,
        verbose_name="منتشر شده؟",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ایجاد",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="آخرین بروزرسانی",
    )


    published_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="زمان انتشار",
    )

    reading_time = models.PositiveIntegerField(
        null=True,
        blank=True,
        verbose_name="زمان مطالعه (دقیقه)",
        help_text="در صورت خالی بودن، به صورت خودکار از روی متن محاسبه می‌شود.",
    )

    # ... created_at, updated_at, Meta, __str__ ...

    def save(self, *args, **kwargs):
        # اگر دستی چیزی وارد نشده بود، خودمون حساب کنیم
        if not self.reading_time and self.content:
            words = len(self.content.split())
            # فرض: حدود ۲۰۰ کلمه در دقیقه
            self.reading_time = max(1, math.ceil(words / 200))
        super().save(*args, **kwargs)





    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ("-created_at",)

    def __str__(self):
        return self.title