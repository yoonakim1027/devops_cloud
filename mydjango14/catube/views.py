from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from catube.models import Video





def index(request: HttpRequest) -> HttpResponse:
    qs = Video.objects.all()
# 이렇게 하면? 이 시점의 코드를 실행한 즉시 실행되는 것이 아님!
    # 실제 값 표출이 필요한 시점까지 최대한 늦췄다가,
    # 응답을 받아서 가져오게 됨 .
    return render(
        request,
        "catube/index.html",{
            "video_list": qs,
        })


# return render(request, 앱이름 한번 써주고 / 생성할 html
# 3번째 인자도 넣을 수 있음. !

