from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # 하나의 테이블에 title,content라는 필드가 있음
    def __str__(self):
        return self.title


# Create your models here.
