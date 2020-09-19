from django.db import models
from django.db.models.constraints import UniqueConstraint 
from django.core.validators import MinValueValidator
from person.models import Person
from stock.models import Stock

# Create your models here.
class SellProductList(models.Model):
	sell_product = models.ForeignKey(Stock, on_delete=models.PROTECT)
	sell_product_quantity = models.IntegerField(default=1,
												validators=[MinValueValidator(limit_value=1)])


class Sell(models.Model):
	person = models.ForeignKey(Person, on_delete=models.PROTECT)
	sell_product_list = models.ForeignKey(SellProductList, on_delete=models.PROTECT, )


	class Meta:
		constraints = [models.UniqueConstraint(fields=["person", "sell_product_list"], 
												name="person_sell_product"), ] 