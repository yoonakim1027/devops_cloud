from django import forms
from shop.models import Shop, Review, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField() # 순수하게 ShopForm에만 존재

    def save(self):
        # 부모의 save를 호출해주어야 합니다.
        saved_post = super().save() #부모의 save가 호출이 됨
        # 부모가 리턴하는 게 있으면, 자식도 똑같이 리턴해줘야 함.
        # 부모가 리턴하는데, 자식이 리턴하지 않으면 사용하는 측에서는 혼란!
        # 자식은 부모가 수행하는 인자, 리턴값을 그대로 따라 주되,
        # 부가적인 연산을 수행할 수 있다.
        # 자식이 부가로 할 일 + 부모가 부가적으로 할 일
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()  # 간단구현을 위해 clear 호출
        saved_post.tag_set.add(*tag_list)

        return saved_post

    # 임의의 이름
    def extra_save(self):
        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()  # 간단구현을 위해 clear 호출
        self.instance.tag_set.add(*tag_list)

    class Meta:
        model = Shop
        # 유저로부터 입력받을 필드 이름을 나열(ip빼고)
        fields = [
            "category",
            "name",
            "description",
            "telephone",
            "photo",

        ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "author_name",
            "message",
        ]
