from django.contrib import admin
from .models import Blog, Category
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Blog)
admin.site.register(Category)
