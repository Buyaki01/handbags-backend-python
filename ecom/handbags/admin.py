from django.contrib import admin

# Register your models here.
# from .models import Products
from .models.products import Products
from .models.category import Category
admin.site.register(Products)
admin.site.register(Category)