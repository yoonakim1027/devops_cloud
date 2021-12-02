from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class pets(models.Model):
    #name, breed, size, neutralOX, weight(중량), 저녁밥 먹는 시간
    created_at = models.DateTimeField(auto_now_add=True) #생성할 때 자동 지정
    updated_at = models.DateTimeField(auto_now=True) # 수정시간 자동 지정

    name = models.CharField(blank=False, null=False, max_length=10, verbose_name="강아지 이름")
    breed = models.CharField(blank=False, null=False, max_length=10, verbose_name="강아지 품종")
    size = models.CharField(blank=False, null=False,max_length=3, verbose_name="강아지 크기")
    birthday = models.DateField(blank=False, null=False,verbose_name="강쥐 생일")
    neutralOX = models.NullBooleanField(blank=False, null=False,verbose_name="중성화 여부")
    weight = models.FloatField(blank=False, null=False,max_length=100, verbose_name="몸무게")
    sleep_time = models.DateTimeField(blank=True, null=True,verbose_name="자는 시간")
    morning_time = models.TimeField(blank=True, null=True, verbose_name="아침밥 먹는 시간")
    dinner_time = models.TimeField(blank=True, null=True, verbose_name="저녁밥 먹는 시간")
    character_of_pets = models.TextField(blank=True, null=True, verbose_name="강아지 성격")


    def __str__(self):
        return self.name