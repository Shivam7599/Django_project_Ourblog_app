# Generated by Django 4.2.3 on 2023-08-03 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Ourblog", "0020_profile_bio"),
    ]

    operations = [
        migrations.RenameField(
            model_name="profile",
            old_name="author",
            new_name="author_name",
        ),
    ]
