from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image', 'created']
    list_filter = ['created']

