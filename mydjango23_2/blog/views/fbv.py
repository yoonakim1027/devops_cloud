from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

# 타입 힌트를 넣으면 좀 더 수월하게 개발할 수 있음
# 최소한 함수의 타입, 리턴타입을 쓰면 오류를 빨리 발견할 수 있음
# 요즘 트랜드는 타입을 다 넣어주는 것
from blog.forms import PostForm
from blog.models import Post


# 조회 (list, detail)
def post_list(request: HttpRequest) -> HttpResponse:
    post_qs = Post.objects.all()

    # print(request.GET)
    # print(request.GET.get("name")) # dict
    # print(request.GET["name"]) # dict
    # print(request.GET.getlist("name")) #  같은 키의 다수 밸류를 지원하는 것

    format = request.GET.get("format", "")
    if format == "xlsx":
        tabular_data = Post.get_tabular_data(post_qs, format="xlsx")
        return HttpResponse(tabular_data, content_type="application/vnd.ms-excel")

    elif format == "json":
        tabular_data = Post.get_tabular_data(post_qs, format="json")
        return HttpResponse(tabular_data, content_type="application/json")

    return render(request, "blog/post_list.html", {
        # 어떤 템플릿에서 사용할 것인지 !
        # 이동하는 것이아니라? 이 템플릿에서 이 경로에 있는 파일을 읽어다가
        # 세번째 인자로 지정한 파일을 읽어다가 템플릿에
        # render가 주체고 얘가 읽어가는 게 중요한 것
        'post_list': post_qs,
    })


# 특정 포스팅에 대한 상세 내역을 보여주는 뷰
# pk 인자가 있어야 조회가 가능
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # Post 인스턴스의 값을 읽어와야 함
    post = get_object_or_404(Post, pk=pk)  # 첫번째 인자 : 어떤 모델에서? 두번째 조건: 어떤 조건에서?
    # 그래서 숫자를 매번 입력할 순 없으니 위에서 받은 pk를 쓰는 것
    # 포스트가 있으면 가져오고, 없으면 404 오류를 뜨게 함
    # 파이썬에서 입력할 때에는 다 그냥 슬러시!
    # 터미널에서는 역슬러시를 씀
    return render(request, "blog/post_detail.html", {
        "post": post,
    })


# 새로생성하는 것은 대상이 없어서 instance를 안씀

# 생성 뷰 -> 생성이기 때문에 pk를 받을 필요가 없음
def post_new(request: HttpRequest) -> HttpResponse:
    # request.method # GET, POST
    if request.method == "POST":
        # 뷰를 사용할 때에는? 항상 GET 요청이 먼저 함
        form = PostForm(request.POST, request.FILES)
        # GET이 아니면 POST라고 생각 !
        # 그럼 if GET이 아니면? POST
        if form.is_valid():
            saved_post = form.save()  # modelForm은 저장된 instance를 반환한다.
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            # return redirect("blog:post_detail", saved_post.pk)
            return redirect(saved_post)

    else:  # 이 쪽이 먼저 실행이 된다
        form = PostForm()
    # 여기에는 값이 하나도 제공되지 않은 상태
    # 값이 없으니까 오류부터 뜰 것
    # 수정이니까 포스트에 대한 pk가 필요함. 수정대상을 알아야 하니까
    return render(request, "blog/post_form.html", {
        "form": form,
    })


# 수정에서는 수정할 게시글이 필요하기 때문에 instance지정이 필요

def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    # 수정 대상을 제공해줘야 함
    post = get_object_or_404(Post, pk=pk)
    # 수정 대상의 모델 인스턴스를 획득

    # request.method # GET, POST
    if request.method == "POST":
        # 뷰를 사용할 때에는? 항상 GET 요청이 먼저 함
        form = PostForm(request.POST, request.FILES, instance=post)  # 인스턴스 꼭 지정!!
        # GET이 아니면 POST라고 생각 !
        # 그럼 if GET이 아니면? POST
        if form.is_valid():
            saved_post = form.save()  # modelForm은 저장된 instance를 반환한다.
            messages.success(request, f"#{pk}번째 포스팅을 저장했습니다.")
            # return redirect("blog:post_detail", saved_post.pk)
            return redirect(saved_post)
            # 이 포스트에 대해서 주소가 필요할때 ? 그냥 redirect 만 있으면 이동 가능


    else:  # 이 쪽이 먼저 실행이 된다
        form = PostForm(instance=post)  # 수정대상을 꼭 지정해줘야 함 ! instance =post
    # 여기에는 값이 하나도 제공되지 않은 상태
    # 값이 없으니까 오류부터 뜰 것
    # 수정이니까 포스트에 대한 pk가 필요함. 수정대상을 알아야 하니까
    return render(request, "blog/post_form.html", {
        "form": form,
    })


# 삭제할 포스팅이 뭔지 알아야 하기 때문에 여기에도 pk가 필요함
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()  # 실제로 DB에 DELETE 쿼리 실행 (즉시삭제)
        messages.success(request, f"#{pk} 포스팅을 삭제했습니다.")
        return redirect("blog:post_list")

    return render(request, "blog/post_confirm_delete.html",
                  {
                      "post": post,

                  })

# 삭제의 프로세스
# GET / POST를 구별 해서 if else
# GET 요청 : 정말 삭제를 할 것인지, 한 번 더 물어본다
# POST 요청 : 삭제를 하고, 다른 주소로 이동을 시킨다
# 삭제했으니까 머무를 이유가 없어서 ~
# 삭제 했으니까 다른 주소, 다른 페이지로 이동 뭐 목록으로 ~ post_list
