import kwargs as kwargs
from django import forms
from zmq.log.__main__ import args

from blog.models import Post, Tag


# modelForm의 관심사는 모델 필드(fields)에만 관심
# 그래서 어떻게 하냐면?
# 초기값지정과 DB로의 저장 설정이 필요하다
# 초기값지정은? 생성자를 통해서 한다.

# 초기값 지정 #
def __init__(self):
    super().__init__(self, *args, **kwargs)  # 몇개를 받았는지는 모르겠지만, 받은 대로 전달하겠다.

    if self.instance.pk:
        tag_qs = self.instance.tag_set.all()
        initial = ",".join([tag.name for tag in tag_qs])  # tag_name 으로 구성된 새로운 커리셋을 만들어서 ,를 구분자로 하나의 리스트를 만들겠다.
        self.fields['tags'].initial = ""  # 생성할때는 초기값 X 수정할때에만 초기값 지정
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

    self.instance.tag_set.clear()
    self.instance.tag_set.add(*tag_list)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "category",
            "title",
            "content",
            "photo",
            "status",

        ]
