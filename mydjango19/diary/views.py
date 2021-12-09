from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

# 포스팅 목록 보여주기
# 모든 함수는 타입을 명시하는 습관을 들여야함!!
from diary.form import PostForm
from diary.models import Post


# 모든 이름은 의미 있게 지어야 한다!!!!!!!!!!!!!!!!!!!!!


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:  # 태그에도 pk가 있긴한데 주로 name으로 씀
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "diary/tag_detail.html", {
        "tag_name": tag_name,
        "post_list": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()  # 전체 포스팅 목록을 얻어올 준비
    # 얻어올 준비라는 것은? 아직 얻어오지 않는다는 것~
    # 요청이 들어올 때에만, 주문이 들어올때에만 하나를 생산하고 추가시킨다 ~

    # 검색 기능 구현 시 추가
    query = request.GET.get("query", "")  # query라는 이름의 값이 있으면 값을 가져오고, 없으면 빈 문자열을 반환
    if query:  # 검색어가 있다면?
        qs = qs.filter(title__icontains=query)
    # 주문이 들어올 때까지 DB에 접근을 안한다!

    context_data = {
        "post_list": qs,  # 이름이 같다고 담고있는 데이터도 같은 것은 아니다!
    }

    return render(request, "diary/post_list.html", {
        "post_list": qs,  # qs 넘겨주기
    })


# render함수는 인자를 총 세개를 가짐
# views가 가진 request, "어떤 경로를 해서 html을 응답", 어떤 랜더링
# 두번째 인자에 꼭 앱이름/모델명_lsit.html

# 모델명_detail(첫번째 인자는 항상 request: HttpRequest) -> HttpResponse
# 두번째 인자는 pk : int (정수)
# detail에서는 두번째 인자가 필요해서, 어떤 링크의 디테일을 보여줄지 pk:int로 받음
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)  # 전체 포스팅 목록을 얻어올 준비
    # 매칭되는 post가 한개이길 기대!
    # pk는 절대 중복될 수 없음!
    # pk에 해당되는 애들은 한개이거나 없거나 둘 중 하나임
    # pk(모델에서 지원하는 필드명, 명시적으로 PK를 조회할거야) = pk

    # 각자의 포스팅에 속한 comment을 받기
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()

    # render(request, 모델명/모델명_detail (템플릿경로)
    # 주문이 들어올 때까지 DB에 접근을 안한다!
    return render(request, "diary/post_detail.html", {
        "post": post,  # qs 넘겨주기
        "comment_list": comment_list,
        "tag_list": tag_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() # ModelForm에서만 지원
            return redirect("diary:post_list")

        else:
            form = PostForm()

    return render(request, "diary/post_form.html", {
        "form": form,
    })


# 수정도 detail처럼 수정대상을 지정하기 위해 pk를 인자로 받아줘야함
def post_edit(request: HttpRequest, pk:int) -> HttpResponse:
    # 아래 코드는 ModelForm에 한해서 동작하는 코드 ! (Form코드는 좀 다름)
    # 수정대상(pk)에 접근해서 읽어옴
    post = Post.objects.get(pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("diary:post_list")

    else:
        form = PostForm(instance=post)

    return render(request, "diary/post_form.html", {
        "form": form,
    })
