from django.db import models







class CarImage(models.Model):
    car = models.ForeignKey(
        "core.Car",
        on_delete=models.CASCADE,
        related_name="images",
        verbose_name="خودرو",
    )
    image = models.ImageField(
        upload_to="cars/gallery/",
        verbose_name="عکس",
    )
    alt_text = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="متن جایگزین (alt)",
    )
    is_primary = models.BooleanField(
        default=False,
        verbose_name="استفاده به‌عنوان تصویر اصلی؟",
    )
    ordering = models.PositiveIntegerField(
        default=0,
        verbose_name="ترتیب نمایش",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="تاریخ افزودن",
    )

    class Meta:
        verbose_name = "عکس خودرو"
        verbose_name_plural = "گالری عکس خودرو"
        ordering = ("ordering", "id")

    def __str__(self):
        return f"عکس {self.car.title}"