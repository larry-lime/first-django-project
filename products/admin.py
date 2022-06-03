from django.contrib import admin

# Register your models here.
from .models import Product, Test
admin.site.register(Product)
admin.site.register(Test)
