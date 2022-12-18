from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Price
from .serializers import ProductSerializer, PriceSerializer


@api_view(['GET'])
def get_all_products(request):
    if request.method == "GET":
        all_products = Product.objects.all()
        serializer = ProductSerializer(all_products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_product(request, product_id):
    if request.method == "GET":
        product = Product.objects.get(pk=product_id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


@api_view(['GET'])
def get_product_prices(request, product_id):
    if request.method == "GET":
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data)
