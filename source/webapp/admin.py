from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'category')


admin.site.register(Product,ProductAdmin)
