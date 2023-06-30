# Generated by Django 4.1.6 on 2023-02-23 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0002_category_delete_categorias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('prod_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='products')),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('actice', models.BooleanField(default=True)),
                ('cat_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='categorias.category')),
            ],
        ),
    ]
