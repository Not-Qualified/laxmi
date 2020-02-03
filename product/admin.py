from django.contrib import admin
from .models import ProductCategory, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_name", "product_type", "product_category", "product_weight"]

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)