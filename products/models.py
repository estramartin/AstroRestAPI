from django.db import models
from categorias.models import Category

# Create your models here.


class Product(models.Model):
    prod_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category, db_column='cat_id',
        null=True, blank=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}: {self.price}'
