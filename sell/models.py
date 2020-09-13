from django.db import models
from django.core.validators import MinValueValidator
from person.models import Person
from stock.models import Stock

# Create your models here.
class Sell(models.Model):
	person = models.ForeignKey(Person, on_delete=models.PROTECT)
	sell_product = models.ForeignKey(Stock, on_delete=models.PROTECT)
	sell_product_quantity = models.IntegerField(default=1, 
												validators=[MinValueValidator(limit_value=0)])
	date_added = models.DateTimeField(auto_now_add=True)