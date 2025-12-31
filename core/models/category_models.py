from django.db import models




class Category(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="عنوان دسته")
    slug = models.SlugField(
        max_length=120,
        unique=True,
        verbose_name="آدرس سئو (slug) دسته",
    )

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"
        ordering = ("title",)

    def __str__(self):
        return self.title