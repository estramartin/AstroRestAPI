from rest_framework.routers import DefaultRouter
from products.Api.views import ProductApiViewSet


ruoter_product = DefaultRouter()

ruoter_product.register(
    prefix='productos', basename='products', viewset=ProductApiViewSet)
