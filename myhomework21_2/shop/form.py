
from django import forms
from shop.models import Shop, Category, Tag

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fiels = [
            "name",
            "description",
            "tag_set",
        ]