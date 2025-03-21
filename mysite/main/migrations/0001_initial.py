# Generated by Django 4.2.11 on 2024-04-23 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PostMain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "slug",
                    models.SlugField(max_length=255, unique=True, verbose_name="Slug"),
                ),
                (
                    "photo",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to="photos/%Y/%m/%d/",
                        verbose_name="Фото",
                    ),
                ),
                ("content", models.TextField(blank=True, verbose_name="Содержание")),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="main_posts",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья о сайте",
                "verbose_name_plural": "Статьи о сайте",
                "ordering": ["-time_create"],
                "indexes": [
                    models.Index(
                        fields=["-time_create"], name="main_postma_time_cr_09393c_idx"
                    )
                ],
            },
        ),
    ]
