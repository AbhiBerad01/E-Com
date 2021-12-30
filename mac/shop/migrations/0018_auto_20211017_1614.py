# Generated by Django 3.2.7 on 2021-10-17 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_product_publ_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 17, 10, 44, 14, 734134, tzinfo=utc)),
        ),
    ]
