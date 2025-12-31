import os
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from .models import Article , Car , CarImage

# حذف عکس قبلی هنگام تغییر عکس
@receiver(pre_save, sender=Article)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_img = Article.objects.get(pk=instance.pk).image
    except Article.DoesNotExist:
        return

    new_img = instance.image
    if old_img and old_img != new_img:
        if os.path.isfile(old_img.path):
            os.remove(old_img.path)


# حذف عکس هنگام حذف مقاله
@receiver(post_delete, sender=Article)
def delete_image_on_article_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)




@receiver(pre_save, sender=Car)
def delete_old_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return

    try:
        old_img = Car.objects.get(pk=instance.pk).main_image
    except Car.DoesNotExist:
        return

    new_img = instance.main_image
    if old_img and old_img != new_img:
        if os.path.isfile(old_img.path):
            os.remove(old_img.path)


# حذف عکس هنگام حذف مقاله
@receiver(post_delete, sender=Car)
def delete_image_on_car_delete(sender, instance, **kwargs):
    if instance.main_image:
        if os.path.isfile(instance.main_image.path):
            os.remove(instance.main_image.path)





# 🔹 تغییر عکس گالری → حذف فایل قدیمی
@receiver(pre_save, sender=CarImage)
def delete_old_gallery_image_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return  # ردیف تازه‌ست

    try:
        old_instance = CarImage.objects.get(pk=instance.pk)
    except CarImage.DoesNotExist:
        return

    old_img = old_instance.image
    new_img = instance.image

    if old_img and old_img != new_img:
        if os.path.isfile(old_img.path):
            os.remove(old_img.path)


# 🔹 حذف فایل گالری هنگام حذف ردیف CarImage
@receiver(post_delete, sender=CarImage)
def delete_gallery_image_on_delete(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
