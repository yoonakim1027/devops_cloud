from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

# 로그인
from django.urls import reverse_lazy
from django.views.generic import CreateView
from PIL import Image

# login view CBV 방식으로 구현
from accounts.forms import LoginForm, SignupFrom

login = LoginView.as_view(
    form_class = LoginForm,
    template_name="accounts/login_form.html",
)


def profile_image(reqest: HttpRequest) -> HttpResponse:
    canvas = Image.new("RGBA", (256, 256), (255, 0, 0, 100))
    # text/image 를 가져올 수 있다

    response = HttpResponse(content_type="image/png")
    canvas.save(response, "PNG")

    return response


# 회원가입 : 새로운 user 인스턴스를 만드는 것 - > CreateView 사용 가능 (클래스)

# FBV 방식 ( 먼저 FBV 방식에 익숙해져야 한다 )

def signup(request):
    if request.method == "POST":
        form = SignupFrom(request.POST, request.FILES)
        if form.is_valid():  # 유효성 검사
            form.save()  # 저장
            return redirect("accounts:login")  # 이동

    else:
        form = SignupFrom()

    return render(
        request,
        "accounts/signup_form.html", {
            "form": form,
        }
    )


#
#
# # 항상 만들때 .as_view가 필요
# # 회원가입을 처리하는 CBV 뷰
# signup = CreateView.as_view(
#     form_class=UserCreationForm,
#     success_url=reverse_lazy("accounts:login"),  # reverse가 되는 시점을 지연시켜야함
#     template_name="accounts/signup_form.html",
# )


# 특정 유저만 볼 수 있는 프로필 페이지. 그 유저만 볼 수 있음
# 구매내역, 회원정보 등~

@login_required  # 로그인이 필요하다 -> 로그인 여부만 확인
def profile(request):
    return render(request, "accounts/profile.html")


# 로그아웃
logout = LogoutView.as_view(
    next_page="accounts:login",  # LogoutView의 next_page는  URl reverse를 지원한다 !
)
