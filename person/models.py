from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator, MaxLengthValidator

# Create your models here.
class Person(models.Model):

	"""
	Person Class - Takes Information such as Name & Contact Detail
	Description - Person can be buyer and seller
	"""

	mobile = RegexValidator(regex="^[1-9]\d{9}$",
							message="Only 10 Digit Mobile Number Allowed")

	pin = RegexValidator(regex="^[1-9]\d{5}$",
							 message="Enter Valid Six Digit PinCode")

	alphabets_only = RegexValidator(regex="^[a-zA-Z]*$",
									message="Only Alphabets Allowed")

	SEX = [("F", "FeMale"), ("M", "Male"), ]

	COUNTRY = [("IND", "India"),
			   ("USA", "United States of America"),
			   ("CAN", "Canada"),
			   ("CHN", "China"), 
			   ("ARE", "United Arab Emirates"), ]

	first_name = models.CharField(max_length=50, 
								  validators=[alphabets_only])
	middle_name = models.CharField(max_length=50, 
								   blank=True, 
								   null=True,
								   validators=[alphabets_only])
	last_name = models.CharField(max_length=50,
								 validators=[alphabets_only])

	sex = models.CharField(max_length=1, choices=SEX)

	job = models.CharField(max_length=30, 
						   blank=True, 
						   null=True, 
						   validators=[alphabets_only],
						   help_text="Onlye Alphabets Allowed")

	mobile_one = models.CharField(max_length=10,
								  validators=[mobile])
	mobile_two = models.CharField(max_length=10,
								  blank=True,
								  null=True,
								  validators=[mobile])

	email = models.EmailField(blank=True, null=True)

	address_one = models.CharField(max_length=100,
								   blank=True, 
								   null=True, )
	address_two = models.CharField(max_length=100,
								   blank=True, 
								   null=True, )

	city = models.CharField(max_length=50,
							validators=[alphabets_only],
							help_text="Only Alphabets Allowed")

	pincode = models.CharField(max_length=6,
							   blank=True,
							   null=True, 
							   validators=[pin])

	country = models.CharField(max_length=3,
							   choices=COUNTRY,
							   default="IND", )

	detail = models.TextField(max_length=300,
							  blank=True, 
							  null=True,
							  validators=[MaxLengthValidator(limit_value=300)],
							  help_text="Maximum 300 Characters Allowed")



	date_added = models.DateTimeField(auto_now_add=True)


	def get_absolute_url(self):
		return reverse("person-detail", kwargs={"pk": self.pk})


	"""
	def __str__(self):
		return f"{self.first_name} {self.last_name}"
	"""
