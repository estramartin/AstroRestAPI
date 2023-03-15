from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from payments.models import Payment
from payments.Api.serializers import PaymentSerializer


class PaymentApiViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['table', 'status_payment']
    Ordering_fields = '__all__'
