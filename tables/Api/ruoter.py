from rest_framework.routers import DefaultRouter
from tables.Api.views import TableApiViewSet

router_table = DefaultRouter()

router_table.register(
    prefix='mesas', basename='Mesas', viewset=TableApiViewSet
)
