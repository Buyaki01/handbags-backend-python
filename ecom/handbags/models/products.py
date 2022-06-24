from django.db import models

from ecom.handbags.models.category import Category
# from .category import Category
  
  
class Products(models.Model):
    name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/')

    def __str__(self):
        return f"{self.title}"