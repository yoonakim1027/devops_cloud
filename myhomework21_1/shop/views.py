from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib import messages
from shop.forms import ShopForm
from shop.models import Shop, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    form = ShopForm(request.POST, request.FILES)
    if form.is_valid():
        saved_post = form.save()

        return redirect("shop:shop_detail", saved_post.pk)


    else:
        form = ShopForm()
    return render(request, "shop/shop_form.html", {
        "form": form,
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
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
        if form.is_valid():
            saved_shop = form.save()
            return redirect("shop:shop_detail", saved_shop.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })

