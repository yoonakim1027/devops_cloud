from django.contrib import admin

from shop.form import ShopForm
from shop.models import Shop, Review, Tag, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm
    # 이 form을 사용해라 !
    list_display = ["name", "description", "telephone", "created_at", "updated_at"]
    list_display_links = ["name"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['shop', 'author_name', 'message', 'created_at']
    list_display_links = ['author_name']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
