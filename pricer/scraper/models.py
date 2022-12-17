from decimal import Decimal

from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Link(models.Model):
    url = models.CharField(max_length=250)
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Price(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    link = models.ForeignKey(
        'Link',
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
