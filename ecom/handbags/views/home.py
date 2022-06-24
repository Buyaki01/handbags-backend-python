from django.shortcuts import render, redirect, HttpResponseRedirect
from rest_framework import viewsets  
from ecom.handbags.models.products import Products
from ecom.handbags.serializers import ProductsSerializer
# from django.views import View
  
# Create your views here.
             
class HomeView(viewsets.ModelViewSet):  
    serializer_class = ProductsSerializer  
    queryset = Products.objects.all()   