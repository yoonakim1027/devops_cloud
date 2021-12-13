from django.db import models

class TimestamedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True


class Shop(TimestamedModel):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    tag_set = models.ManyToManyField('Tag',blank=True)


class Category(TimestamedModel):
    name = models.CharField(max_length=100, unique=True)


class Tag(TimestamedModel):
    name = models.CharField(max_length=100, unique=True)

