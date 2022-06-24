from rest_framework import serializers

from ecom.handbags.models.products import Products

class ProductsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Products
    fields = '__all__'