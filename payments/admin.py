from django.contrib import admin
from payments.models import Payment


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['pay_id', 'table',
                    'status_payment', 'payment_type', 'created_at']
