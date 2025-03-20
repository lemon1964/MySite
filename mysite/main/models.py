from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth import get_user_model
from posts.models import translit_to_eng


# Модель для главных постов
class PostMain(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None,
                              blank=True, null=True, verbose_name="Фото")
    content = models.TextField(blank=True, verbose_name="Содержание")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='main_posts', null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья о сайте"
        verbose_name_plural = "Статьи о сайте"
        ordering = ['time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post_main', kwargs={'post_slug': self.slug})

    def save(self, *args, **kwargs):
        temp = self.title.split()
        if len(temp) > 1:
            temp = temp[:2]
        temp = " ".join(temp)
        self.slug = slugify(translit_to_eng(temp))
        super().save(*args, **kwargs)
