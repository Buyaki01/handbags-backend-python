from django.db import models
import datetime
from ecom.handbags.models.products import Products
from ecom.handbags.models.user import User
  
class Order(models.Model):
  product = models.ForeignKey(Products, on_delete=models.CASCADE)
  customer = models.ForeignKey(User, on_delete=models.CASCADE)
  quantity = models.IntegerField(default=1)
  price = models.IntegerField()
  address = models.CharField(max_length=50, default='', blank=True)
  phone = models.CharField(max_length=50, default='', blank=True)
  date = models.DateField(default=datetime.datetime.today)
  status = models.BooleanField(default=False)