# Generated by Django 3.2.7 on 2021-10-17 10:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_blogpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='publ_date',
            field=models.DateField(default=datetime.datetime(2021, 10, 17, 10, 44, 14, 878644, tzinfo=utc)),
        ),
    ]