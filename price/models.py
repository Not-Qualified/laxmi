from django.db import models
from django.urls import reverse

# Create your models here.
class Price(models.Model):
	gold_market_price = models.DecimalField(max_digits=21, decimal_places=2)
	gold_bill_price = models.DecimalField(max_digits=21, decimal_places=2)
	gold_old_ornaments_price = models.DecimalField(max_digits=21, decimal_places=2)
	gold_24_carat = models.DecimalField(max_digits=21, decimal_places=2)
	gold_22_carat = models.DecimalField(max_digits=21, decimal_places=2)
	gold_18_carat = models.DecimalField(max_digits=21, decimal_places=2)


	silver_without_bill_price = models.DecimalField(max_digits=21, decimal_places=2)
	silver_with_bill_price = models.DecimalField(null=True, blank=True, 
												max_digits=21, decimal_places=2, 
												default=0.00)

	date_added = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse("price-detail", kwargs={"pk": self.pk})

"""
	def get_absolute_url(self):
		return reverse("price-list")
"""