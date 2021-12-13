from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

# 새로운 Shop 등록 페이지
# 바뀌는 인자가 없기 때문에, pk를 안받아도 돼
# /shop/new/
from pyexpat.errors import messages

from django.contrib import messages

from shop.form import ShopForm, ReviewForm
from shop.models import Shop, Review, Tag, Category


# list
def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all()

    category_id = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)  # 필터링 수행
    # __ 언더바 두개는 카테고리 모델로 들어가게되는 것
    query = request.GET.get("query", "")  # query라는 이름의 값이 있으면 값을 가져오고, 없으면 빈 문자열을 반환
    if query:  # 검색어가 있다면?
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "category_list": category_qs,
        "shop_list": qs,

    })


# form - shop
def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()  # 항상 저장이 먼저임
            # commit=False가 되면, 할당을 못받기 때문에 안돼 !! 무조건 비어있는 상태로

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
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
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

def review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=post_pk)

    # 입력서식 만들기
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # 유효성 검사를 하고,  다 성공해야지만 is_vaild() 실행.
            review = form.save(commit=False)  # 유효성검사에 다 통과된 데이터만 저장됨
            review.post = shop  # post모델 인스턴스
            review.save()

        return redirect("shop:shop_detail", post_pk)
        # 저장되면 해당 post_detail로 넘어감
    else:
        form = ReviewForm()
    # 템플릿에서 사용할 값을 이름과 함께 넘겨줘야만,
    # 템플릿에서 그 이름으로 접근할 수 있는 것
    return render(request, "shop/review_form.html", {
        "form": form,

    })
    # _form.html은 하나의 약속임


# /diary/100/comments/20/edit
def review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    # 지정 pk에 Comment가 없으면 404 오류가 뜨게 !
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect("shop:shop_detail", post_pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, "shop/review_form.html", {
        "form": form,  # 수정 서식만 보여줌.
    })
