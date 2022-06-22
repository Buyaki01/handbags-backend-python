from django.shortcuts import render, redirect, HttpResponseRedirect
from ..serializers import ProductSerializer 
from rest_framework import viewsets   
# from django.views import View
from ..models import Products   
  
# Create your views here.
             
class HomeView(viewsets.ModelViewSet):  
    serializer_class = ProductSerializer   
    queryset = Products.objects.all()   