from django.db import models


class ContactMessage(models.Model):
    SUBJECT_CHOICES = (
        ("buy", "خرید خودرو"),
        ("sell", "فروش خودرو"),
        ("stock", "سوال درباره موجودی"),
        ("feedback", "پیشنهاد یا انتقاد"),
    )

    name = models.CharField(
        max_length=100,
        verbose_name="نام و نام خانوادگی",
    )

    phone = models.CharField(
        max_length=20,
        verbose_name="شماره تماس",
    )

    subject = models.CharField(
        max_length=20,
        choices=SUBJECT_CHOICES,
        verbose_name="موضوع",
    )

    city = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="شهر",
    )

    message = models.TextField(
        verbose_name="متن پیام",
    )

    notify_me = models.BooleanField(
        default=False,
        verbose_name="اطلاع‌رسانی درباره خودروهای مشابه",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ ارسال",
    )

    class Meta:
        verbose_name = "پیام تماس"
        verbose_name_plural = "پیام‌های تماس"
        ordering = ("-created_at",)

    def __str__(self):
        return f"{self.name} - {self.get_subject_display()}" # type: ignore 
