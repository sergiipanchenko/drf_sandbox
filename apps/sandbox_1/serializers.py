from rest_framework import serializers
from .models import Product, HistoryProductPrice


class HistoryProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryProductPrice
        fields = ('price', 'date')


class ProductSerializer(serializers.ModelSerializer):
    history_price = HistoryProductPriceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'history_price')
