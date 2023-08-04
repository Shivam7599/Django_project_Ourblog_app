# Generated by Django 4.2.1 on 2023-07-30 04:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Ourblog", "0005_alter_poster_category_alter_poster_title_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="poster",
            name="likes",
            field=models.ManyToManyField(
                related_name="Blog_post", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
