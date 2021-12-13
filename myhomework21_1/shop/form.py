from django import forms
from shop.models import Shop, Category, Tag


class ShopForm(forms.ModelForm):
    # tag
    tags = forms.CharField()

    class Meta:
        model = Shop

        fields = [
            "category",
            "name",
            "description",
        ]
