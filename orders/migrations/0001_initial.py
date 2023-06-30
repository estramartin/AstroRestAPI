# Generated by Django 4.1.6 on 2023-02-28 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
        ('products', '0003_rename_actice_product_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('ord_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('PENDING', 'pendiente'), ('DELIVERED', 'delivered')], max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('close', models.BooleanField(default=False)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.product')),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tables.table')),
            ],
        ),
    ]
