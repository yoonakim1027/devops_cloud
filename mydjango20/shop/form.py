from django import forms
from shop.models import Shop, Review, Tag


class ShopForm(forms.ModelForm):
    tags = forms.CharField()  # 순수하게 ShopForm에만 존재

    # 부모 클래스의 생성자에서 어떤 인자를 지원하는 지는 잘 모르겠지만,
    # 생성자 호출 시에 받은 인자 그대로
    # 부모에게 전달하겠다.

    # 태그 이름이 수정 시에 남게 하기
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # tags는 우리가 Form 클래스에 직접 추가한 필드니까
        # 초기값도 우리가 직접 지정해주어야 한다.

        # ShopForm의 tags 필드 초기값을 생성자를 통해서 지정
        if self.instance.pk:  # 수정 시
            tag_qs = self.instance.tag_set.all()  # 다가져오기
            tags = ",".join([tag.name for tag in tag_qs])  # tag.name으로만 구성된 리스트

            self.fields["tags"].initial = tags
        else:  # 새롭게 작성 시
            pass

    # .initial : 특정 필드에 대해서 필드 초기값을 지정하는 것

    # 여러개로 나눠진 인자를 한 개로 팩(모으는 것)
    # 그래서 받을 때 *args 팩
    # 하단의 super 줄은 언팩
    # 호출할 때 쓰는 것은 언팩

    def save(self):
        # 부모의 save를 호출해주어야 합니다.
        saved_post = super().save()  # 부모의 save가 호출이 됨
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
