from django.db import models



class Tag(models.Model):
    TAG_TYPE_CHOICES = (
        ("car", "خودرو"),
        ("article", "مقاله"),
    )

    tag_type = models.CharField(
        max_length=20,
        choices=TAG_TYPE_CHOICES,
        verbose_name="نوع تگ",
        default="car",  # برای مایگریشن اولیه، می‌تونی car بذاری
    )

    title = models.CharField(max_length=50, unique=True, verbose_name="عنوان تگ")
    slug = models.SlugField(
        max_length=60,
        unique=True,
        verbose_name="آدرس سئو (slug) تگ",
    )

    class Meta:
        verbose_name = "تگ"
        verbose_name_plural = "تگ‌ها"
        ordering = ("title",)

    def __str__(self):
        return self.title
    


