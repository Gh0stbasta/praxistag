from django.shortcuts import render
from .models import products
from rest_framework.generics import ListAPIView
from .serializer import ProductSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView



class ProductListView(ListAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductCreateView(CreateAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(RetrieveAPIView):
    queryset = products.objects.all()
    serializer_class = ProductSerializer
