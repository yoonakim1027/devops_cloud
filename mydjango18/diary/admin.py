from django.contrib import admin

from diary.models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author_name", "created_at", "updated_at"]
    list_display_links = ["title"]


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'post', 'message', 'created_at']
    list_display_links = ['post']


@admin.register(Tag)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']