from django import forms
from diary.models import Post


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
