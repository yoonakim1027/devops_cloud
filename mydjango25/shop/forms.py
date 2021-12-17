
from django import forms

from shop.models import Review


class ReviewForm(forms.ModelForm):
    class Meta: # 이 클래스에 대한 옵션을 지정
        model = Review
        fields = [
            'message',

        ] # fields는 리스트 형식으로 써야한다