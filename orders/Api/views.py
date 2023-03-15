from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from orders.Api.serializers import OrderSerializer
from orders.models import Order


class OrderApiViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('-ord_id')
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['table', 'status', 'close', 'payment']
    ordering_fields = '__all__'
