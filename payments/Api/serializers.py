from rest_framework.serializers import ModelSerializer
from tables.Api.serializers import TableSerializer
from payments.models import Payment


class PaymentSerializer(ModelSerializer):
    table_data = TableSerializer(source='table', read_only=True)

    class Meta:
        model = Payment
        fields = ['pay_id', 'table', 'table_data', 'total_payment',
                  'payment_type', 'status_payment', 'created_at']
