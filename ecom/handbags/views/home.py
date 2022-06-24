from django.shortcuts import render, redirect, HttpResponseRedirect
from rest_framework import viewsets
from rest_framework import generics
from handbags.serializers import ProductsSerializer
from handbags.models.products import Products 

# from django.views import View
  
# Create your views here.
             
class HomeView(generics.ListAPIView):  
  serializer_class = ProductsSerializer
  queryset = Products.objects.all()  
    
