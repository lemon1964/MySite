# Generated by Django 4.2.11 on 2024-04-26 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="postmain",
            options={
                "ordering": ["time_create"],
                "verbose_name": "Статья о сайте",
                "verbose_name_plural": "Статьи о сайте",
            },
        ),
    ]
