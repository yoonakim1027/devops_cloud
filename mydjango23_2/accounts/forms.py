from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


# 회원가입 폼
# TODO : email을 추가로 입력받으려 합니다.
#       User 모델에 대한  ModelForm
#       -Meta.fields = > ['username'] #현재는 username뿐. 여기에 email필드를 넣으면 알아서 뜰 것
#        -추가 form fields => password1, password2
class SignupFrom(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # model폼을 상속받으려면 .Meta까지 써줘야 함
        fields = ['username', 'email']  # 필드를 추가적으로 정의


class LoginForm(AuthenticationForm):
    answer = forms.CharField(
        # required=False,
        label="퀴즈 답",
        help_text="3+3=?",

    )

    def clean_answer(self):
        answer = self.cleaned_data.get("answer")
        if answer != '6':  # 6이 아닐때는?
            raise forms.ValidationError("땡~~~!")
        return answer  # 항상 값 리턴을 가져와야 함 !
