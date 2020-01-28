from django.urls import path
from .views import (CreatePersonView, ListPersonView, DetailPersonView, 
					UpdatePersonView, DeletePersonView, 
                    )

urlpatterns = [
    path("", CreatePersonView.as_view(), name="person-create"),
    path("list/", ListPersonView.as_view(), name="person-list"),
    path("detail/<int:pk>/", DetailPersonView.as_view(), name="person-detail"),
    path("update/<int:pk>/", UpdatePersonView.as_view(), name="person-update"),
    path("delete/<int:pk>/", DeletePersonView.as_view(), name="person-delete"),
]
