from django.contrib import admin

# Register your models here.
from yoona.models import Post

# admin이랑 쌍을 지어주려고 postadmin!
class PostAdmin(admin.ModelAdmin):
    list_display = ["title",  "created_at"]
# 실제 모델에 있는 필드명을 써야 함!

    search_fields = ['title']
admin.site.register(Post, PostAdmin)
# 이렇게 하면 기본적인 admin 옵션만 등록