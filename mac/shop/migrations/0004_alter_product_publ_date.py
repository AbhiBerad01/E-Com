# Generated by Django 3.2.7 on 2021-09-28 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210928_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 9, 28, 19, 11, 44, 580336), verbose_name='Date'),
        ),
    ]
