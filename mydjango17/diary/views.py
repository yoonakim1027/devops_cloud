from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# 포스팅 목록 보여주기
# 모든 함수는 타입을 명시하는 습관을 들여야함!!
from diary.models import Post


# 모든 이름은 의미 있게 지어야 한다!!!!!!!!!!!!!!!!!!!!!

def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()  # 전체 포스팅 목록을 얻어올 준비
    # 얻어올 준비라는 것은? 아직 얻어오지 않는다는 것~
    # 요청이 들어올 때에만, 주문이 들어올때에만 하나를 생산하고 추가시킨다 ~

    # 주문이 들어올 때까지 DB에 접근을 안한다!
    return render(request, "diary/post_list.html", {
        "post_list": qs,  # qs 넘겨주기
    })
# render함수는 인자를 총 세개를 가짐
# views가 가진 request, "어떤 경로를 해서 html을 응답", 어떤 랜더링
# 두번째 인자에 꼭 앱이름/모델명_lsit.html
