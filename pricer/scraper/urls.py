from django.urls import path

from . import views

urlpatterns = [
    path('products', views.get_all_products, name='products'),
    path('products/<int:product_id>', views.get_product, name='product'),
    path('products/prices/<int:product_id>', views.get_product_prices, name='product_prices'),
]
