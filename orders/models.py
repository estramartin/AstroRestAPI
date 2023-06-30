from django.db import models
from tables.models import Table
from products.models import Product
from payments.models import Payment

StatusEnum = (("PENDING", "pendiente"), ("DELIVERED", 'delivered'))


class Order(models.Model):
    ord_id = models.AutoField(primary_key=True)
    table = models.ForeignKey(
        Table, on_delete=models.SET_NULL, db_column='tab_id', null=True, blank=True)
    product = models.ForeignKey(
        Product, db_column='prod_id', on_delete=models.SET_NULL, null=True, blank=True)
    payment = models.ForeignKey(
        Payment, db_column='pay_id', on_delete=models.CASCADE, null=True, blank=True)

    status = models.CharField(max_length=255, choices=StatusEnum)
    created_at = models.DateTimeField(auto_now_add=True)
    close = models.BooleanField(default=False)

    def __str__(self):
        return str(self.table.number)
