from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	product_category = models.CharField(max_length=50, )

	def __str__(self):
		return f"{self.product_category}"


class Product(models.Model):

	p_type = [("G", "Gold"), ("S", "Silver"), ("O", "Other")]

	product_name = models.CharField(max_length=50, )
	product_type = models.CharField(max_length=1, choices=p_type)
	product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
	product_weight = models.DecimalField(max_digits=21, decimal_places=3)