from decimal import Decimal

from django.db import models


def product_directory_path(instance, filename):
    return 'products/{0}/{1}'.format(instance.name, filename)


class Product(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to=product_directory_path, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Link(models.Model):
    url = models.CharField(max_length=250)
    product = models.ForeignKey(
        'Product',
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.url}'


class Price(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    link = models.ForeignKey(
        'Link',
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}'
