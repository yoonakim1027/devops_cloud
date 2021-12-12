from django import forms
from shop.models import Shop, Review, Tag


class ShopForm(forms.ModelForm):
    class Meta: #form에 대한 옵션 적용
        model = Shop
        fields = "__all__"

