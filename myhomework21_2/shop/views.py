from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpRequest, HttpResponse

from shop.form import ShopForm
from shop.models import Shop, Category, Tag


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    category_qs = Category.objects.all()

    category_id:str = request.GET.get("category_id","")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    if query:
        qs = qs.filter(name__icontains=query)




    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "category_list":category_qs,
    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html", {
        "shop": shop,

    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_vaild():
            saved_post = form.save()
            return redirect("shop:shop_detail", saved_post.pk)
        else:
            form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def shop_edit(request:HttpRequest, pk:int)->HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    if request.method =="POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)
    else:
        form = ShopForm(instance=shop)

    # 유효성 검사
    if form.is_valid():
        saved_shop = form.save()
        messages.success(request,".성공적으로 수정했습니다.")
        return redirect("shop:shop_detail",saved_shop.pk)