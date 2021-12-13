from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from shop.form import ShopForm
from shop.models import Shop, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()

    ## 검색기능
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            # shop_detail 뷰를 구현했다면 !!!
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)  # 수정대상을 알아야 하니까
    # 내가 가져올 모델의 대상을 확실히 인지하고 써야함.

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)  # instance = 수정대상
    else:
        form = ShopForm(instance=shop)

    # 유효성 검사
    if form.is_valid():
        saved_shop = form.save()
        # 저장했으니 이제 이동하겠다.
        messages.success(request, "성공적으로 수정했습니다.")
        return redirect("shop:shop_detail", saved_shop.pk)
