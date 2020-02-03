from django.shortcuts import render
from django.views.generic import (CreateView, ListView, )
from .models import Product, ProductCategory
# Create your views here.

class CreateProductView(CreateView):
	model = Product
	fields = ["product_name", "product_type", "product_category", "product_weight"]


class ListProductView(ListView):
	model = Product