from rest_framework.routers import DefaultRouter
from orders.Api.views import OrderApiViewSet


router_order = DefaultRouter()

router_order.register(prefix='pedidos', basename='orders',
                      viewset=OrderApiViewSet)
