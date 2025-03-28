from django.contrib import admin
from .models import PostMain

@admin.register(PostMain)
class PostMainAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'photo']
    list_display = ('title', 'time_create') 
    prepopulated_fields = {"slug": ("title", )}

