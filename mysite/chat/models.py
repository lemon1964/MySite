# chat/models.py
from django.db import models
from users.models import User
# from django.contrib.auth.models import User
from courses.models import Course
from django.utils import timezone


class CourseChat(models.Model):
    course = models.ForeignKey(Course, related_name='course_chat', on_delete=models.CASCADE)
    messages = models.TextField(default='')
    created_at = models.DateTimeField(default=timezone.now)
    

    def __str__(self):
        return f"Chat for {self.course}"

