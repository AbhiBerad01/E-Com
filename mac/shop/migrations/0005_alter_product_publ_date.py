# Generated by Django 3.2.7 on 2021-09-28 13:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_publ_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 28, 19, 23, 26, 384284), verbose_name='Date'),
        ),
    ]
