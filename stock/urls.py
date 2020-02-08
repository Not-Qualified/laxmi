from django.urls import path
from .views import (CreateStockView, ListStockView, )

urlpatterns = [
	path("create/", CreateStockView.as_view(), name="stock-create"),
	path("list/", ListStockView.as_view(), name="stock-list"),
]