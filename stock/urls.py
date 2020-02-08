from django.urls import path
from .views import (CreateStockView, ListStockView, 
					UpdateStockView, DetailStockView, 
					DeleteStockView, )

urlpatterns = [
	path("create/", CreateStockView.as_view(), name="stock-create"),
	path("list/", ListStockView.as_view(), name="stock-list"),
	path("update/<int:pk>/", UpdateStockView.as_view(), name="stock-update"),
	path("detail/<int:pk>/", DetailStockView.as_view(), name="stock-detail"),
	path("delete/<int:pk>/", DeleteStockView.as_view(), name="stock-delete"),
]