from django.urls import path
from .views import (CreateProductView, ListProductView, 
					UpdateProductView, DetailProductView, 
					DeleteProductView, 
					)

urlpatterns = [
	path("create/", CreateProductView.as_view(), name="product-create"),
	path("list/", ListProductView.as_view(), name="product-list"),
	path("update/<int:pk>/", UpdateProductView.as_view(), name="product-update"),
	path("detail/<int:pk>/", DetailProductView.as_view(), name="product-detail"),
	path("delete/<int:pk>/", DeleteProductView.as_view(), name="product-delete"),
]