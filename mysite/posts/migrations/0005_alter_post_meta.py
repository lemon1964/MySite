# Generated by Django 4.2.20 on 2025-04-01 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0004_alter_comment_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="meta",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="metadata",
                to="posts.metadata",
                verbose_name="Метаданные",
            ),
        ),
    ]
