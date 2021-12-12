from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# 새로운 Shop 등록 페이지
# 바뀌는 인자가 없기 때문에, pk를 안받아도 돼
# /shop/new/
from pyexpat.errors import messages

from django.contrib import messages

from shop.form import ShopForm, ReviewForm
from shop.models import Shop, Review, Tag


# list
def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("query", "")  # query라는 이름의 값이 있으면 값을 가져오고, 없으면 빈 문자열을 반환
    if query:  # 검색어가 있다면?
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })


# form - shop
def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            shop = form.save(commit=False)
            shop.ip = request.META['REMOTE_ADDR']
            shop.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("shop:shop_list")

    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


# /shop/100/
def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "review_list": review_list,
        "tag_list": tag_list,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)  # 수정대상(pk)에 접근해서 읽어옴

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_post = form.save(commit=False)
            return redirect("shop:shop_list")

    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:  # 태그에도 pk가 있긴한데 주로 name으로 씀
    qs = Shop.objects.all()
    qs = qs.filter(tag_set__name=tag_name)
    return render(request, "shop/tag_detail.html", {
        "tag_name": tag_name,
        "shop_list": qs,
    })


# form - shop


def review_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError('곧 구현 예정') # 예외를 발생시키는 raise

    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            saved_review = review_form.save()
            # shop 디테일 뷰를 구현했다면 ?
            return redirect("shop:shop_detail", saved_review.pk)


    else:
        review_form = ReviewForm()
    return render(request, "shop/review_form.html", {
        "review_form": review_form,  # 빈 서식 만들기
    })


def review_edit(request: HttpRequest, pk: int) -> HttpResponse:
    review = Review.objects.get(pk=pk)

    if request.method == "POST":
        review_form = ShopForm(request.POST, request.FILES, instance=review)
        if review_form.is_valid():
            saved_review = review_form.save(commit=False)
            return redirect("shop:shop_detail", saved_review.pk)

    else:
        review_form = ShopForm(instance=review)

    return render(request, "shop/shop_form.html", {
        "review_form": review_form,
    })
