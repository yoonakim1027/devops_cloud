from django.contrib import admin
from shop.models import Shop, Category, Tag
from shop.forms import ShopForm


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
	form = ShopForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass
