from datetime import datetime

import django
from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=5000)
    desc = models.CharField(max_length=8000)
    price = models.IntegerField(default=0)
    publ_date = models.DateField(default=django.utils.timezone.now())
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    image = models.ImageField(upload_to="shop/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    item_json = models.CharField(max_length=50000, default="")
    name = models.CharField(max_length=500, default="")
    amount = models.IntegerField(default=0)
    email = models.CharField(max_length=500, default="")
    phone = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=5000, default="")
    city = models.CharField(max_length=500, default="")
    state = models.CharField(max_length=500, default="")
    zip_code = models.CharField(max_length=50, default="")


class OrderUpdate(models.Model):
    update_id = models.BigAutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=50000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:12] + "..."
