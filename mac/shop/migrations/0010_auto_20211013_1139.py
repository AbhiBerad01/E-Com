# Generated by Django 3.2.7 on 2021-10-13 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_publ_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(default='', max_length=50000)),
                ('name', models.CharField(default='', max_length=500)),
                ('email', models.CharField(default='', max_length=500)),
                ('phone', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=5000)),
                ('city', models.CharField(default='', max_length=500)),
                ('state', models.CharField(default='', max_length=500)),
                ('zip_code', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 13, 11, 39, 15, 682282), verbose_name='Date'),
        ),
    ]