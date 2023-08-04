from django.contrib import admin

# Register your models here.

from .models import Poster, Category, Comment, Profile
admin.site.register(Poster)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Profile)
