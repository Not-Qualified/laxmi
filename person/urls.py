from django.urls import path
from .views import (CreatePersonView, ListPersonView, DetailPersonView, 
					#UpdateCustomerView, DeleteCustomerView, 
                    )

urlpatterns = [
    path("", CreatePersonView.as_view(), name="person-create"),
    path("list/", ListPersonView.as_view(), name="person-list"),
    path("detail/<int:pk>/", DetailPersonView.as_view(), name="person-detail"),
    #path("update/<int:pk>/", UpdateCustomerView.as_view(), name="customer-update"),
    #path("delete/<int:pk>/", DeleteCustomerView.as_view(), name="customer-delete"),
]
