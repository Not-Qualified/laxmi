from django.db import models
from django.core.validators import (RegexValidator, MinLengthValidator, 
									MaxLengthValidator, )


class ProductCategory(models.Model):
	p_category = RegexValidator(regex="^([A-Za-z0-9\-\ ]+)$")

	product_category = models.CharField(max_length=50, unique=True,
										validators=[p_category, 
													MinLengthValidator(limit_value=3),
													MaxLengthValidator(limit_value=50), ])

	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"{self.product_category}"


class Product(models.Model):

	p_type = [("G", "Gold"), ("S", "Silver"), ("O", "Other")]

	p_name = RegexValidator(regex="^([A-Za-z0-9\-\ ]+)$", 
							message="Only Letters, Numbers and Hyphen(-) Allowed")

	product_name = models.CharField(max_length=50, unique=True,
									validators=[p_name, 
									MinLengthValidator(limit_value=3),
									MaxLengthValidator(limit_value=50), ])
	product_type = models.CharField(max_length=1, choices=p_type)
	product_category = models.ForeignKey(ProductCategory, 
										 on_delete=models.PROTECT)
	product_weight = models.DecimalField(max_digits=21, decimal_places=3)

	date_added = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		pass