from django import forms
from shop.models import Shop, Category, Tag, Review

# 한 세트!
class ShopForm(forms.ModelForm):
# 초기값 넣어주기
    tags = forms.CharField()

    def __init__(self,*args, **kwargs):
        super().__init__(*args,**kwargs)

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            tags = ",".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags

# DB 저장하기
    def save(self):
        saved_post = super().save() #부모 호출해서 부모가 하는일

        # 자식이 하는 일
        tag_list =[]
        tags = self.cleaned_data.get("tags","")
        for word in tags.split(","):
            tag_name = word.strip()
            tag,__ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear() # 구현을 간단하게 하기 위해. 일단 다 지우고 add
        saved_post.tag_set.add(*tag_list)
        return saved_post

    class Meta:
        model = Shop
        fields = [
            "category",
            "name",
            "description",
        ]



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["author_name", "message"]