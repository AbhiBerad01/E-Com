# Generated by Django 3.2.7 on 2021-10-17 07:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_alter_product_publ_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 17, 7, 2, 27, 661461, tzinfo=utc)),
        ),
    ]
