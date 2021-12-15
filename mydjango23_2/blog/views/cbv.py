# Class Based View(CBV)
#   - 뷰 함수를 만들어 주는 클래스


# post_list
# post_list 라는 무언가가 생성되는 것
from django.shortcuts import resolve_url
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.forms import PostForm
from blog.models import Post

# post_list(이쪽이 뷰 함수) 오른쪽의 리턴 값이 왼쪽
post_list = ListView.as_view(
    model=Post,
)

# post_detail
post_detail = DetailView.as_view(
    model=Post,

)


# post_new
# 방금 생성한 포스팅의 detail로 들어가고 싶다 !
# 매번 유동적으로 url이 바뀜

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):  # 함수는 필요할 때 마다 호출
        post_pk = self.object.pk  # 장고가 기본 구현한 모델 인스턴스가 저장됨
        # 방법 1 (인자를 넘기는 방법의 차이 )
        return reverse_lazy("blog:post_detail", args=[post_pk])
        # 리턴 값 : 문자열

        # 방법 2 # 내부적으로 reverse를 사용
        # return resolve_url("blog:post_detail",post_pk)
        # 리턴 값 : 문자열
        # 기능이 좀 더 많다 .

        # 방법 3
        # return redirect("blog:post_detail",post_pk)
        # 리턴 값 : HttpResponse
        # 뷰 함수에서 리턴할 때 사용

        # 방법 4
        # {% url "blog_detail" post_pk %}
        # 리턴 값 : 문자열
        # -> 템플릿에서 링크만들 때 사용

    # 얘는 url이 고정되어 있음
    # success_url = reverse_lazy("blog:post_list")


post_new = PostCreateView.as_view()


# post_edit

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm

    # def get_success_url(self):
    #     post_pk = self.object.pk
    #     return reverse("blog:post_detail", args=[post_pk])


post_edit = PostUpdateView.as_view(
    # TODO : 가변적으로 URL을 지정할 수 없다.
    # TODO : URL Reverse가 미적용.
    # 밑에는 직접 적용한 것임.
    # success_url= "blog:post_list"# 성공했을 시 이동할 url
    # success_url은 url Reverse를 지원하지 않음.
    # 완성된 문자열 url을 가져와야 함

    # success_url=reverse("blog:post_list")
    # reverse()가 이 이름으로 url reverse하는 것. 역할이 같음
    # 근데 이렇게 하면 동작이 안됨

    success_url=reverse_lazy("blog:post_list")
    # 그래서 reverse_lazy를 사용

    # reverse()는 즉시 실행 -> 프로젝트 로딩중에는 url reverse를 할 수 없어서 reverse가 실패하는 것
    # reverse_lazy()는 늦게 실행. 프로젝트가 다 로딩된 이후에, success_url이 필요할 때 동작됨
    # 시점이 문제임 !!
)

# post_delete

post_delete = DeleteView.as_view(
    model=Post,
    success_url=reverse_lazy("blog:post_list")

)

# fbv 함수를 잘 다룰 수 있을 때가 되면 cbv 연습하기
