from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from catube.models import Video



# generic -> 범용적으로 쓸 수 있는 것
# Class Based View(CBW) -> class 기반 뷰

index = ListView.as_view(model=Video,
                         template_name = "catube/index.html")

# Function Based View (FBV) -> 함수 기반 뷰
# def index(request: HttpRequest) -> HttpResponse:
#     qs = Video.objects.all()
# # 이렇게 하면? 이 시점의 코드를 실행한 즉시 실행되는 것이 아님!
#     # 실제 값 표출이 필요한 시점까지 최대한 늦췄다가,
#     # 응답을 받아서 가져오게 됨 .
#     return render(
#         request,
#         "catube/index.html",{
#             "video_list": qs,
#         })


# return render(request, 앱이름 한번 써주고 / 생성할 html
# 3번째 인자도 넣을 수 있음. !

def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    # 함수가 호출될때, url에서 pk에 해당하는 문자열을 뽑아와서 그걸로
    # DB에서 찾는것
    return render(
                  request,
                  "catube/video_detail.html",
        {
            "video" : video,
        },)
    #render는 인자가 세개다 !