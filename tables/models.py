from django.db import models

# Create your models here.


class Table(models.Model):
    tab_id = models.AutoField(primary_key=True)
    number = models.IntegerField()

    def __str__(self):
        return str(self.number)
