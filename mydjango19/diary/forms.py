from django import forms
from diary.models import Post,Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        # 유저로부터 입력받을 필드 이름을 나열(ip빼고)
        fields = [
            "author_name",
            "title",
            "content",
            "photo",
            "tag_set",
        ]
        # 나는 여기에 명시한 필드들의 값들만 받겠다!!!!


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields는 리스트가 아님
       # fields = "__all__" #이렇게 지정하는 것이 약속임
        # 모든 필드의 정보를 읽어오게 하는 것
        fields =['author_name','message']

        # 항상 오타 확인, forms 이름 !!

