from django.db import models
from tables.models import Table


paymentTypeEnum = (
    ('CARD', 'card'),
    ('CASH', 'cash')
)

paymentStatusEnum = (
    ('PENDING', 'pending'),
    ('PAID', 'paid')
)


class Payment(models.Model):
    pay_id = models.AutoField(primary_key=True)
    table = models.ForeignKey(
        Table, db_column='tab_id', on_delete=models.SET_NULL, null=True)
    total_payment = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.CharField(max_length=255, choices=paymentTypeEnum)
    status_payment = models.CharField(
        max_length=255, choices=paymentStatusEnum)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.table)
