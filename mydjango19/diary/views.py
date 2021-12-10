from idlelib.autocomplete import FILES

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from diary.form import PostForm, CommentForm
from diary.models import Post
from django.contrib import messages


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:  # 태그에도 pk가 있긴한데 주로 name으로 씀
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "diary/tag_detail.html", {
        "tag_name": tag_name,
        "post_list": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    context_data = {
        "post_list": qs,
    }
    return render(request, "diary/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()

    return render(request, "diary/post_detail.html", {
        "post": post,  # qs 넘겨주기
        "comment_list": comment_list,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # ModelForm에서만 지원
            post.ip = request.META['REMOTE_ADDR']
            post.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("diary:post_list")

    else:
        form = PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })


# 수정도 detail처럼 수정대상을 지정하기 위해 pk를 인자로 받아줘야함
def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드 ! (Form코드는 좀 다름)
    # 수정대상(pk)에 접근해서 읽어옴
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect("diary:post_list")

    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })


# 두번째 인자는 가변적으로 바뀌는 url
# 가변적으로 바뀌는 부분을 캡쳐
# -> 캡쳐해서, 어떤 특정 이름으로 장고가 넘겨주도록 할 수 있음

# /diary/100/comments/new/
# -> HttpResponse 리턴타입임
def comment_new(request: HttpRequest, post_pk:int) -> HttpResponse:
    # 입력서식 만들기
    if request.method =="POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
        # 유효성 검사를 하고,  다 성공해야지만 is_vaild() 실행.
            saved_comment = form.save() # 유효성검사에 다 통과된 데이터만 저장됨
            # 저장된 comment만
        return redirect("diary:post_detail",post_pk)
        # 저장되면 해당 post_detail로 넘어감
    else:
        form = CommentForm()
    # 템플릿에서 사용할 값을 이름과 함께 넘겨줘야만,
    # 템플릿에서 그 이름으로 접근할 수 있는 것
    return render(request, "diary/comment_form.html", {
        "form": form,

    })
    # _form.html은 하나의 약속임


# /diary/100/comments/20/edit
def comment_edit(request: HttpRequest, post_pk:int, pk:int) -> HttpRequest:
    pass
