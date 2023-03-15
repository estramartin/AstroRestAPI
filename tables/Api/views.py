from tables.Api.serializers import TableSerializer
from tables.models import Table
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class TableApiViewSet(ModelViewSet):
    queryset = Table.objects.all().order_by('tab_id').order_by('number')
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number']
