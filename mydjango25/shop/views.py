# CBV 방식으로 구현
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse, request
from django.shortcuts import redirect, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# class명.view()
from shop.forms import ReviewForm
from shop.mixins import ReviewUserCheckMixin
from shop.models import Shop, Category, Review


# ListView를 상속받음
class ShopListView(ListView):
    model = Shop
    # 페이징 : 한 페이지에 몇개씩 보여줄지?
    paginate_by = 5

    # 원래 이 함수는 모든 클래스 기반 뷰에 다 존재함
    # 템플릿에서 사용할 변수목록(사전)을 만들어주는 함수
    def get_context_data(self, **kwargs):
        # 부모가 인자를 받은데로, 자식이 재구현
        # 밑의 context_data는 사전
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = Category.objects.all()
        return context_data


# 여러 줄 쓸 때에는 보통 콤마를 마지막에 씀.
# 동작에는 영향은 없음

shop_list = ShopListView.as_view(
    model=Shop,
    # 리스트 뷰에서 필수적인 속성은 모델 !
    # 다른 것들은 다 옵션임 - > 안쓰면 적용될 디폴트 값이 존재하다는 뜻
    template_name="shop/shop_list.html"

)

# template_name = 모델명/생성할템플릿이름.html 쓰면
# 생성할 수 있음

shop_detail = DetailView.as_view(
    # DetailView에선, 어떤 뷰에대한 Detail인지 모델 지정이 필요
    model=Shop,
    template_name="shop/shop_detail.html"
)


# 상점과 리뷰간의 관계는 1 :N
# 리뷰에 샵이라는 외래키만 생성하면?
# 샵 측에 shop.review_set (리뷰셋이 들어가있음)이라는 것이 생성
# 그래서 여기에 shop.review_set.all()을 쓰면 내용 다 가져올 수 있음

# 여기에 현재 로그인이 되었을 때에만 리뷰를 쓰게 하려면?
# class ReviewCreateView(LoginRequiredMixin,CreateView):
# 첫번째 인자로 LoginRequiredMixin 사용
class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm

    # FIXME : shop detail로 이동
    success_url = reverse_lazy("shop:shop_list")

    # 유효성 검사에 통과한다면?
    # form_class -> success_url
    def form_valid(self, form) -> HttpResponse:
        # urls.py에 shop_pk는 어디에 저장되었냐면?
        # self.kwargs : URL Captured 값들이 사전으로 저장
        shop_pk = self.kwargs['shop_pk']  # 이렇게 접근하면 현재 접근한 url의 pk를 얻을 수 있음
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()
        # 이제 shop_detail로 이동하면 좋겠다~
        return redirect(shop)


# TODO : shop_detail로 이동
# (1) 먼저 shop_list로 연결
review_new = ReviewCreateView.as_view()


# 로그인을 해야 댓글을 수정할 수 있게 하려면 ?
# 그러면 custom class  view를 만들어야 함

# 이렇게 되면 클래스의 부모가 둘! -> 다중 상속 (두개 이상 가능)
# 언어에 따라 다중상속을 지원하는 언어가 다름 ~

# UserPassesTestMixin 로그인 했는지 안했는지 결정
class ReviewUpdateView(LoginRequiredMixin, ReviewUserCheckMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    # FIXME : shop detail로 보내기
    # success_url = reverse_lazy("shop:shop_list")

    def get_success_url(self):
        review = self.object
        return resolve_url(review.shop)#주소
# 자기가 수정할 수 있는 리뷰만 볼 수 있게 하려면 ?


# 이렇게 하면? 로그인 안하면 댓글 수정이 안됨
review_edit = ReviewUpdateView.as_view()
