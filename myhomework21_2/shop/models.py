from django.db import models


class TimestamedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestamedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-id']  # 정렬
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"


class Shop(TimestamedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-id']  # 정렬
        verbose_name = "상점"
        verbose_name_plural = "상점 목록"



class Tag(TimestamedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']  # 오름정렬
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
