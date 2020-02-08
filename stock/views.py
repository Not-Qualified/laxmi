from django.shortcuts import render
from django.views.generic import (CreateView, ListView, UpdateView,
									DetailView, DeleteView, )
from .models import Stock
# Create your views here.
class CreateStockView(CreateView):
	model = Stock
	fields = ["product", "product_quantity"]


class ListStockView(ListView):
	model = Stock


class UpdateStockView(UpdateView):
	model = Stock
	fields = ["product", "product_quantity"]


class DetailStockView(DetailView):
	model = Stock


class DeleteStockView(DeleteView):
	model = Stock
	success_url = "/"