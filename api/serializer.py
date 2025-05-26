from .models import products
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = [
            'id',
            'name',
            'short_description',
            'product_description',
            'stock',
            'price'
        ]
