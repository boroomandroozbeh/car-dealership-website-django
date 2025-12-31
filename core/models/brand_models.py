from django.db import models



class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام برند")
    slug = models.SlugField(max_length=120, unique=True, verbose_name="آدرس سئو (slug)")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"
        ordering = ("name",)

    def __str__(self):
        return self.name