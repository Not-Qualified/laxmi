from django.urls import path
from .views import (CreatePriceView, ListPriceView, 
					UpdatePriceView, DetailPriceView, 
					DeletePriceView, )

urlpatterns = [
	path("create/", CreatePriceView.as_view(), name="price-create"),
	path("list/", ListPriceView.as_view(), name="price-list"),
	path("update/<int:pk>/", UpdatePriceView.as_view(), name="price-update"),
	path("detail/<int:pk>/", DetailPriceView.as_view(), name="price-detail"),
	path("delete/<int:pk>/", DeletePriceView.as_view(), name="price-delete"),
]