from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('id', 'category', 'name', 'slug', 'description', 'price', 'stock', 'available', 'created', 'updated')
