from django.contrib import admin

from .models import Image


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["title", "user", "created", "slug"]
    list_filter = ["created"]
    search_fields = ["title"]
