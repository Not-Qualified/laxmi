from django.contrib import admin
from .models import Price
# Register your models here.

class PriceAdmin(admin.ModelAdmin):
	list_display = ("date_added", "gold_market_price")
admin.site.register(Price, PriceAdmin)