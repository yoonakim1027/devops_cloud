from django.db import models
import datetime
# Create your models here.
from django.db.models import ImageField


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=13)

    photo = ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)