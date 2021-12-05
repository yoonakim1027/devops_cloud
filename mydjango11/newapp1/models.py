from django.db import models

# Create your models here.
class cute_dog(models.Model):
    #name, breed, size
    name = models.CharField(max_length=100, verbose_name="강아지 이름")
    breed = models.CharField(max_length=100, verbose_name="강아지 품종")
    size = models.CharField(max_length=11, verbose_name="강아지 크기")
    birthday = models.DateField()



