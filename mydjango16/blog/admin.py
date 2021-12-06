from django.contrib import admin

from blog.models import Post, Comment, Tag


# 등록을 위해서는? 각각의 모델 마다 등록이 필요
# 등록하는 방법은 admin.site.register

@admin.register(Post)  # 장식자 이용하기
class PostAdmin(admin.ModelAdmin):  # 상속문법
    pass


# 각각 하나씩 만들어줘야함
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'post', 'message', 'created_at']


# 각 모델의 admin -> 상속을 받아야 함

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
