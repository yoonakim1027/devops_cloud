from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from diary.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    context_data = {
        "post_list": qs,
    }
    return render(request, 'diary/post_list.html', {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)  # 전체 포스팅 목록을 얻어올 준비

    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()

    return render(request, "diary/post_detail.html", {
        "post": post,  # qs 넘겨주기
        "comment_list": comment_list,
        "tag_list": tag_list,
    })
