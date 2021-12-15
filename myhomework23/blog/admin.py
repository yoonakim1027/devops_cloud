from django.contrib import admin

# Register your models here.
from blog.models import Post, Category, Comment, Tag


@admin.register(Post)
class ShopAdmin(admin.ModelAdmin):
	pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	pass



@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass
