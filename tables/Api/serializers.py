from rest_framework.serializers import ModelSerializer
from tables.models import Table


class TableSerializer(ModelSerializer):
    class Meta:
        model = Table
        fields = ['tab_id', 'number']
