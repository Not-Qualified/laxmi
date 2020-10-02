from django.shortcuts import render
from django.views.generic import (CreateView, ListView, UpdateView, 
								  DetailView, DeleteView)
from .models import Product, ProductCategory

# Create your views here.

class CreateProductView(CreateView):
	model = Product
	fields = ["product_name", 
				"product_type", 
				"product_category", 
				"product_specification", 
				"product_gross_weight", 
				"product_other_weight", 
				"product_net_weight", 
				"product_seller", 
				"product_labour", 
				"product_other_charge_diamond", 
				"product_other_charge_rodium", 
				"product_other_charge_pearl", 
				"product_measurement", ]


class ListProductView(ListView):
	model = Product


class UpdateProductView(UpdateView):
	model = Product
	fields = ["product_name", 
				"product_type", 
				"product_category", 
				"product_specification", 
				"product_gross_weight", 
				"product_other_weight", 
				"product_net_weight", 
				"product_seller", 
				"product_labour", 
				"product_other_charge_diamond", 
				"product_other_charge_rodium", 
				"product_other_charge_pearl", 
				"product_measurement", ]


class DetailProductView(DetailView):
	model = Product


class DeleteProductView(DeleteView):
	model = Product
	success_url = "/"


class CreateProductCategoryView(CreateView):
	model = ProductCategory
	fields = ["product_category"]


class ListProductCategoryView(ListView):
	model = ProductCategory


class UpdateProductCategoryView(UpdateView):
	model = ProductCategory
	fields = ["product_category"]


class DetailProductCategoryView(DetailView):
	model = ProductCategory


class DeleteProductCategoryView(DeleteView):
	model = ProductCategory
	success_url = "/"
