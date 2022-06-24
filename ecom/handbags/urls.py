from django import views
from django.contrib import admin
from django.urls import path
from .views.home import HomeView
app_name = 'handbags' 

# from .views.signup import Signup
# from .views.login import Login, logout
# from .views.cart import Cart
# from .views.checkout import CheckOut
# from .views.orders import OrderView
# from .middlewares.auth import auth_middleware
# from . import views
  
urlpatterns = [
  path('', HomeView.as_view()),
]
