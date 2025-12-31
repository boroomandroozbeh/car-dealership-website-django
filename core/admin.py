from django.contrib import admin
from core.models import Brand, Car, Feature, Category, Tag, Article, CarImage
from .models import ContactMessage

# Register your models here.


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "subject", "created_at", "notify_me")
    list_filter = ("subject", "notify_me", "created_at")
    search_fields = ("name", "phone", "message")
    ordering = ("-created_at",)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    search_fields = ("title",)


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1
    fields = ("image", "alt_text", "is_primary", "ordering")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "brand",
        "year",
        "city",
        "price",
        "is_active",
        "is_featured",
    )
    list_filter = ("brand", "year", "city", "gear_type", "is_active", "is_featured")
    search_fields = ("title", "model", "city", "description")
    prepopulated_fields = {"slug": ("title",)}
    list_editable = (
        "is_active",
        "is_featured",
    )
    filter_horizontal = ("features", "tags")
    ordering = ("-created_at",)
    inlines = [CarImageInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "is_published", "created_at")
    list_filter = ("category", "is_published", "created_at")
    search_fields = ("title", "summary", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("tags",)  # برای انتخاب راحت تگ‌ها
