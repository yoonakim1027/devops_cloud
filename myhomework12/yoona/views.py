from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from yoona.models import Post

def index(request):
    return render(request, "yoona/index.html")
# render(인자 두개만 넣음)

def post_list(request: HttpRequest) -> HttpResponse:

   # request.GET #QueryString Values
    #request.POST # Post 요청 Values
    #request.FILES # Post 요청에서 파일 Values


    # blog/templates/blog/post_list.html
    qs = Post.objects.all() # querySet Type
    qs = qs.order_by("-pk")
    # pk : 오름차순 / -pk : pk필드에 대한 내림차순

    q = request.GET.get("q", "")# 하나의 사전
    if q: # filter를 함으로써 where 조건이 지정됨
        qs = qs.filter(title__icontains=q)
# q라는 문자열이 포함이 된다면?
    # i -> ignore 대소문자를 구별하지 않겠다
    return render(request, "yoona/post_list.html", {
        "post_list": qs,
    }) #두번째 인자에 앱이름


def post_detail(request: HttpRequest, pk:int) -> HttpResponse:
    # pk = 1 #pk -> primary key
    post = Post.objects.get(pk=pk) # 변수명으로 대체
    return render(request, "yoona/post_detail.html",{
        "post": post,
    })
