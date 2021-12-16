from django import forms

from shop.models import Shop, Category, Review, Tag


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
