from django.shortcuts import render
from django.views.generic import (CreateView, ListView, DetailView, 
								  UpdateView, DeleteView, )
from .models import Person

# Create your views here.
class CreatePersonView(CreateView):
	model = Person
	fields = ["first_name", "middle_name", "last_name", "sex", "job",
			  "mobile_one","mobile_two", "email", "address_one", "address_two",
			  "pincode", "city", "country", "detail", ]


class ListPersonView(ListView):
	model = Person
	ordering = ["-date_added"]


class DetailPersonView(DetailView):
	model = Person


"""
class UpdateCustomerView(UpdateView):
	model = Customer
	fields = ["first_name", "middle_name", "last_name", "sex", "job",
			  "mobile_one","mobile_two", "email", "address_one", "address_two",
			  "pincode", "city", "country", "detail", ]


class DeleteCustomerView(DeleteView):
	model = Customer
	success_url = "/"
"""