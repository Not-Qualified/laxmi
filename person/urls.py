from django.urls import path
from .views import (CreatePersonView, #ListCustomerView, DetailCustomerView, 
					#UpdateCustomerView, DeleteCustomerView, 
                    )

urlpatterns = [
    path("", CreatePersonView.as_view(), name="person-create"),
    #path("list/", ListCustomerView.as_view(), name="customer-list"),
    #path("detail/<int:pk>/", DetailCustomerView.as_view(), name="customer-detail"),
    #path("update/<int:pk>/", UpdateCustomerView.as_view(), name="customer-update"),
    #path("delete/<int:pk>/", DeleteCustomerView.as_view(), name="customer-delete"),
]
