from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from diary.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()  # 전체 포스팅 목록을 얻어올 준비
    context_data = {
        "post_list": qs,
    }
    query = request.GET.get("query", "")  # query라는 이름의 값이 있으면 값을 가져오고, 없으면 빈 문자열을 반환
    if query:  # 검색어가 있다면?
        qs = qs.filter(title__icontains=query)

    return render(request, "diary/post_list.html", {
        "post_list": qs,  # qs 넘겨주기
    })



def post_detail(request: HttpRequest, pk: int) -> HttpResponse:

    post = Post.objects.get(pk=pk)		# 전체 포스팅 목록을 얻어올 준비
    templates_name = "diary/post_list.html"
    context_data = {
        "post": post,
    }

    # 각자의 포스팅에 속한 comment을 받기
    comment_list = post.comment_set.all() # 위에서 얻어온 포스팅 목록의 post
    tag_list = post.tag_set.all()

    # render(request, 모델명/모델명_detail (템플릿경로)
    # 주문이 들어올 때까지 DB에 접근을 안한다!
    return render(request, "diary/post_detail.html", {
        "post": post,  # qs 넘겨주기
        "comment_list": comment_list,
        "tag_list": tag_list,
    })