from django.contrib import admin
from .models import Item, Review

class ReviewInline(admin.TabularInline):
    model = Review

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
    list_display = ("name", "price")

admin.site.register(Item, ItemAdmin)