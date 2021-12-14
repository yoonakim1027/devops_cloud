from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpRequest, HttpResponse

from shop.form import ShopForm, ReviewForm
from shop.models import Shop, Category, Tag, Review


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    category_qs = Category.objects.all()

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "category_list": category_qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    review_list = shop.review_set.all()
    tag_list = shop.tag_set.all()

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "review_list": review_list,
        "tag_list": tag_list,
    })


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


# 디비 에러
# shop_id shop이라는 오류

def review_new(request: HttpRequest, post_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=post_pk)

    # 입력서식 만들기
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            # 유효성 검사를 하고,  다 성공해야지만 is_vaild() 실행.
            review = form.save(commit=False)  # 디비 지정 지연 # 유효성검사에 다 통과된 데이터만 저장됨
            review.shop = shop  # post모델 인스턴스
            review.save()

        return redirect("shop:shop_detail", post_pk)
        # redirect : 저장되면 해당 post_detail로 넘어감
    else:
        form = ReviewForm()
    # 템플릿에서 사용할 값을 이름과 함께 넘겨줘야만,
    # 템플릿에서 그 이름으로 접근할 수 있는 것
    return render(request, "shop/review_form.html", {
        "form": form,

    })


def review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)

    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect("shop:shop_detail", post_pk)
            # redirect : 주소로 연결
    else:
        form = ReviewForm(instance=review)  # 수정대상 review

    return render(request, "shop/review_form.html", {
        "form": form,
    })
