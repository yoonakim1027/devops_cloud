from django import forms
from shop.models import Shop, Category, Tag


class ShopForm(forms.ModelForm):

    tags =forms.CharField()
    def save(self):
        saved_post = super().save()
        tag_list =[]
        tags = self.cleaned_data.get("tags","")
        for word in tags.split(","):
            tag_name = word.strip()
            tag,__ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()
        saved_post.tag_set.add(*tag_list)
        return saved_post

    class Meta:
        model = Shop
        fields = [
            "name",
            "description",
            "tag_set",
        ]
