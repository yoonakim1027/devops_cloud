from django.contrib import admin

from shop.models import Shop, Category, Tag, Review


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "created_at", "updated_at"]
    list_display_links = ["name"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin): # 해당 지정 모델이 admin에서 구동할때
    list_display = ['name']
    list_display_links = ['name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['shop', 'author_name', 'message', 'created_at']
    list_display_links = ['author_name']

