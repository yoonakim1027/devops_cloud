from django.contrib import admin
from dog.models import Post, Comment


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "updated_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'post', 'message', 'created_at']
    list_display_links = ['post']