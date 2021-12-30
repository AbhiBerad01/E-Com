import django
from django.db import models
from datetime import datetime


# Create your models here.

class Blogpost(models.Model):
    post_id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=5000)
    heading0 = models.CharField(max_length=8000)
    c_heading0 = models.CharField(max_length=8000)
    heading1 = models.CharField(max_length=8000)
    c_heading1 = models.CharField(max_length=8000)
    heading2 = models.CharField(max_length=8000)
    c_heading2 = models.CharField(max_length=8000)
    publ_date = models.DateField(default=django.utils.timezone.now())
    thumbnail = models.ImageField(upload_to="blogs/images", default="")

    def __str__(self):
        return self.title
