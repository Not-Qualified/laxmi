from django.urls import path
from .views import (CreateProductView, ListProductView, 
					#UpdatePriceView, DetailPriceView, 
					#DeletePriceView, 
					)

urlpatterns = [
	path("create/", CreateProductView.as_view(), name="product-create"),
	path("list/", ListProductView.as_view(), name="product-list"),
	#path("update/<int:pk>/", UpdatePriceView.as_view(), name="price-update"),
	#path("detail/<int:pk>/", DetailPriceView.as_view(), name="price-detail"),
	#path("delete/<int:pk>/", DeletePriceView.as_view(), name="price-delete"),
]