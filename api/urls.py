from django.contrib import admin
from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView
from django.http import HttpResponse
# from .dataInjection import *


def hello(request):
    return HttpResponse("Welcome to the API")

urlpatterns = [
    path('', hello, name="hello"),
    path('products/', ProductListView.as_view(), name="all_products"),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('products/create', ProductCreateView.as_view(), name="create_product")
]