from django.db import models

# Create your models here.
from django.db.models import ImageField


class Shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    photo = ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)