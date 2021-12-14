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


def review_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():  # 유효성 검사 호출
            saved_review = review_form.save()
            return redirect("shop:shop_detail", saved_review.pk)

        else:
            review_form = ReviewForm()

        return render(request, "shop/review_form.html", {
            "review_form": review_form,
        })


def review_edit(request:HttpRequest,shop_pk:int, pk:int)-> HttpResponse:
    review = get_object_or_404(Review,pk=pk)

    if request.method =="POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect("shop:shop_detail",shop_pk)

        else:
            form = ReviewForm(instance=review) #수정대상 review

        return render(request, "shop/review_form.html",{
            "form":form,
        })