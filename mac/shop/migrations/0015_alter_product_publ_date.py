# Generated by Django 3.2.7 on 2021-10-16 15:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_product_publ_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 16, 15, 30, 59, 575782, tzinfo=utc)),
        ),
    ]
