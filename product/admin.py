from django.contrib import admin
from .models import ProductCategory, Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	list_display = ["product_name", 
					"product_type", 
					"product_category", 
					"product_specification", 
					"product_gross_weight", 
					"product_other_weight", 
					"product_net_weight", 
					"product_seller", 
					"product_labour", 
					"product_other_charge_diamond", 
					"product_other_charge_rodium", 
					"product_other_charge_pearl", 
					"product_measurement", ]

admin.site.register(ProductCategory)
admin.site.register(Product, ProductAdmin)