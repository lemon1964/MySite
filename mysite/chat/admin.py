from django.contrib import admin
from .models import CourseChat


@admin.register(CourseChat)
class CourseChatAdmin(admin.ModelAdmin):
    list_display = ['course', 'created_at']