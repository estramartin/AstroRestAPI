# Generated by Django 4.1.6 on 2023-02-26 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('tab_id', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.IntegerField()),
            ],
        ),
    ]