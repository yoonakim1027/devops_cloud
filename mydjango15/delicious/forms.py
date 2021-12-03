from django import forms
# 장고에서 지원해주는 forms이라는 기능 사용


from delicious.models import Shop

class ShopForm(forms.ModelForm):
    # 클래스 생성 -> 클래스의 부모는? forms.ModelForm -> 이거를 인자로 넣음
    class Meta:
        model = Shop
        fields = "__all__"