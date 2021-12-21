from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from dog.models import Post


def post_list(request:HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)
    context_data = {
        'post_list' : qs, # 키 : 값
    }
    return render(request, 'dog/post_list.html',context_data)


def post_detail(request:HttpRequest, pk:int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    templates_name = "dog/post_list.html"

    context_data = {
        "post":post,
    }

    return render(request,'dog/post_detail.html', context_data)