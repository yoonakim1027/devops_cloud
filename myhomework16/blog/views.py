from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from blog.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    context_data = {
        "post_list": qs, # 키 : 값
    }
    return render(request, "blog/post_list.html", context_data)


def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    templates_name = 'blog/post_list.html'
    context_data = {
        "post": post,
    }
    return render(request, 'blog/post_detail.html',context_data)