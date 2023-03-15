from rest_framework.routers import DefaultRouter
from payments.Api.views import PaymentApiViewSet


router_payment = DefaultRouter()


router_payment.register(
    prefix='pagos', basename='payments', viewset=PaymentApiViewSet)
