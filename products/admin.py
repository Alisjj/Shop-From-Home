from django.contrib import admin
from .models import Category, Item, Review, UploadImage



class ReviewInline(admin.TabularInline):
    model = Review

class ImageInline(admin.TabularInline):
    model = UploadImage

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
        ImageInline,
    ]
    list_display = ("name", "price")

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
