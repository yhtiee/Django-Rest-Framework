from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.createProduct, name="create"),
    path("get/", views.getProducts, name="get")
]
