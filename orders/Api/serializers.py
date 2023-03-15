from rest_framework.serializers import ModelSerializer
from tables.Api.serializers import TableSerializer
from products.Api.serializers import ProductSerliazer
from orders.models import Order


class OrderSerializer(ModelSerializer):
    data_table = TableSerializer(source='table', read_only=True)
    data_product = ProductSerliazer(source='product', read_only=True)

    class Meta:
        model = Order
        fields = ['ord_id',
                  'status', 'created_at', 'close', 'payment',
                  'table', 'data_table', 'product', 'data_product']
