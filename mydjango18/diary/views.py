from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# list_list.html 생성
from diary.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()  # 전체 포스팅 얻어올 준비
    context_data = {
        "post_list": qs,
    }
    # 검색 구현 기능 시 필요
    query = request.GET.get('query','')
    if query:
        qs = qs.filter(title__icontains=query)

    # 여기서 context_data로 받는 이유는 return할때 render 함수를 쓸 건데
    # 여기서 필요한 게 사전 형식으로 받은 데이터임

    return render(request, "diary/post_list.html",
                  {
                      "post_list": qs,  # qs넘겨주기
                  })


# 여기서는 인자를 두 개 받아야 함. detail은 인자가 두개 필요해!
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    templates_name = 'diary/post_list.html'
    context_data = {
        "post": post,
    }
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()

    return render(request, 'diary/post_detail.html',{
        "post": post,
        "comment_list":comment_list,
        "tag_list":tag_list,
    })