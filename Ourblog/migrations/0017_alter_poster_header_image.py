# Generated by Django 4.2.3 on 2023-08-01 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ourblog", "0016_alter_poster_header_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="poster",
            name="header_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
