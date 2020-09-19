from django.contrib import admin
from .models import Sell, SellProductList
# Register your models here.
# class SellProductListInline(admin.StackedInline):
# 	model = SellProductList
# 	extra = 3

# class SellAdmin(admin.ModelAdmin):
# 	list_display = ("person", "sell_product_list")	
# 	inlines = [SellProductListInline]


admin.site.register(Sell, )
admin.site.register(SellProductList)