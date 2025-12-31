from django.db import models



class Feature(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name="نام آپشن")

    class Meta:
        verbose_name = "آپشن"
        verbose_name_plural = "آپشن‌ها"
        ordering = ("title",)

    def __str__(self):
        return self.title