from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse

# 제가 만들 뷰 목록 : post_list, post_detail, post_new, post_edit, post_delete
from blog.forms import PostForm
from blog.models import Post, Category


def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()

    # 검색기능 구현
    query = request.GET.get("query", "")
    if query:
        post_qs = post_qs.filter(name__icontains=query)

    # 카테고리 구현
    category_qs = Category.objects.all()
    category_id: str = request.GET.get("category_id", "")
    if category_id:
        post_qs = post_qs.filter(category__pk=category_id)

    return render(request, "blog/post_list.html", {
        "post_list": post_qs,
        "category_list": category_qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    tag_list = post.tag_set.all()

    return render(request, "blog/post_detail.html", {
        "post": post,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_vaild():
            saved_post = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect(saved_post)

    else:
        form = PostForm()

    return render(request, "blog/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect(saved_post)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_form.html', {
        "form": form,
        "post": post,
    })


def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        messages.success(request, f"{pk} 포스팅을 삭제했습니다.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html", {
        "post": post,
    })
