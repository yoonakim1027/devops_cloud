import re

from django import forms

from blog.models import Post, Tag, Subscriber




class PostForm(forms.ModelForm):
    tags = forms.CharField() # 데이터 받기
    # modelForm의 관심사는 모델 필드(fields)에만 관심
    # 그래서 어떻게 하냐면?
    # 초기값지정과 DB로의 저장 설정이 필요하다
    # 초기값지정은? 생성자를 통해서 한다.

    # 초기값 지정 #
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 몇개를 받았는지는 모르겠지만, 받은 대로 전달하겠다.

        if self.instance.pk:
            tag_qs = self.instance.tag_set.all()
            initial = ",".join([tag.name for tag in tag_qs])  # tag_name 으로 구성된 새로운 커리셋을 만들어서 ,를 구분자로 하나의 리스트를 만들겠다.
            self.fields['tags'].initial = initial  # 생성할때는 초기값 X 수정할때에만 초기값 지정
            # 이렇게 하면 tags 필드에서 초기값을 지정할 수 있게 됨

    # 우리가 태그스를 DB에 저장하려고 하면? tags는 ManyToMany
    # 이 포스트가 DB에 저장이되어야지만(기본키가 있어야지만) tag와 관계를 맺을 수 있음
    # 관계라는 것은? post의 pk와 tag의 pk를 비교해서 하는 것

    # DB로의 저장 #

    # def save(self, commit=True): # 일반 필드에서 할때는 이것을 호출
    def _save_m2m(self):  # ManyToMany필드에서는 이것을 사용
        # 이것의 역할은? 함수가 호줄되기전에, 항상 instance.save()가 호출되어서 pk가 항상 있는 상황임
        super()._save_m2m()  # save
        # 이것은 리턴값이 없어서 로직만 처리
        # 부모를 보고, 부모의 행동대로 자식도 구현해주는 것
        tag_list = []  # tag 인스턴스로만 구성된 리스트
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        self.instance.tag_set.clear()
        self.instance.tag_set.add(*tag_list)

    # cleaned_data -> 정제된 데이터(변환된 데이터 -> form에서 값을 변환을 하고나면?
    # cleaned -> 변환
    # content에 스크립트 태그가 들어가면 제거하는 함수
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if content:
            # script 태그를 제거
            content = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.I | re.S)
        return content

    class Meta:
        model = Post
        fields = [
            "category",
            "title",
            "content",
            "photo",
            "status",

        ]


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"

    # 원본이 필요할 때도 있지만, 왠만해서는 cleaned_data를 써서 접근해야 함
    # Form 만의 유효성 검사 방법 + 데이터 변환 기능 제공
    def clean_phone(self):
        phone = self.cleaned_data.get("phone")  # 데이터 꺼내기
        if phone:  # phone 값이 있을 때
            if not phone.startswith("010"):  # 어떤 문자열이 ""로 시작한다면?
                raise forms.ValidationError("전화번호는 010으로 시작토록 입력해주세요.")

        return phone.replace("-", "")  # 값을 변환해서 리턴.
        # DB에는 -이 빠진 번호가 저장되게 됨

        # 폰번호가 우리가 원하는 값의 형태가 아니라고 한다면?
