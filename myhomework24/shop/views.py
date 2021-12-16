from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop.forms import ShopForm, ReviewForm
from shop.models import Shop, Tag, Review, Category

# #  shop
# list
shop_list = ListView.as_view(
    model=Shop,
)

# detail
shop_detail = DetailView.as_view(
    model=Shop,

)


# new 구현을 위한 class 생성
class ShopCreateView(CreateView):
    model = Shop
    form_class = ShopForm


shop_new = ShopCreateView.as_view(

)


# edit 구현을 위한 class 생성
class ShopUpdateView(UpdateView):
    model = Shop
    form_class = ShopForm


shop_edit = ShopUpdateView.as_view(
    success_url=reverse_lazy("shop:shop_list")
    # 프로젝트가 로딩될 때까지 기다렸나가 나중에 실행
)

# delete
shop_delete = DeleteView.as_view(
    model=Shop,
    success_url=reverse_lazy("shop:shop_list")
    # 삭제 후 list로 이동하는 이유는 삭제 했으면 해당하는 detail 페이지가 없기 때문에
)


# review_new, review_edit, review_delete 뷰 구현
# # Review

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm


review_new = ReviewCreateView.as_view()


class ReviewUpdateView(UpdateView):
    model = Review
    form_class = ReviewForm



# review_edit = ReviewUpdateView.as_view(
#     success_url=reverse_lazy("shop:shop_detail")
# )

review_delete = DeleteView.as_view(
    model=Review,
    success_url=reverse_lazy("shop:shop_list")
)
