from django import forms

from shop.models import Shop, Category, Review, Tag


class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = "__all__"

    tags = forms.CharField()

    def save(self):
        saved_shop = super().save()

        # tag 로직
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()  # 좌우 공백을 제거
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_shop.tag_set.clear()
        saved_shop.tag_set.add(*tag_list)

        return saved_shop




class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
