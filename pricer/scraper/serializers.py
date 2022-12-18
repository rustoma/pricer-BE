from rest_framework import serializers

from .models import Product, Price, Link


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Link
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    link = LinkSerializer()

    class Meta:
        model = Price
        fields = '__all__'
