# Generated by Django 4.1.6 on 2023-02-23 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_cat_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='actice',
            new_name='active',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='cat_id',
            new_name='category',
        ),
    ]
