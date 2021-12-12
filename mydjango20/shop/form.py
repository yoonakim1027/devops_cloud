from django import forms
from shop.models import Shop, Review, Tag


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        # 유저로부터 입력받을 필드 이름을 나열(ip빼고)
        fields = [
            "name",
            "description",
            "telephone",
            "photo",
            "tag_set",
        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {
            "author_name",
            "message",
        }
