from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from product.models import Product
# Create your models here.
class Stock(models.Model):
	product = models.OneToOneField(Product, on_delete=models.PROTECT)
	product_quantity = models.IntegerField(default=0, 
										   validators=[MinValueValidator(limit_value=0)])

	def __str__(self):
		return f"{self.product}"

	def get_absolute_url(self):
		return reverse("stock-detail", kwargs={"pk": self.pk})