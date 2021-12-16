from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpRequest, HttpResponse

from shop.forms import ShopForm
from shop.models import Shop, Tag, Comment, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    category_qs = Category.objects.all()
    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)
    # category 컬럼에서 __pk가 있는지 검사 하고 category_id와 같은지 확인

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
        "tag_list": tag_list,
    })


def shop_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        # 유효성 검사 : .is_valid()
        if form.is_valid():
            saved_shop = form.save()
            messages.success(request, "새로운 포스팅을 저장했습니다.")
            return redirect(saved_shop)
    else:  # 들어온 요청이 GET일 경우
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=shop)

        # 유효성 검사
        if form.is_valid():
            saved_shop = form.save()
            messages.success(request, "성공적으로 수정했습니다.")
            return redirect(saved_shop)


    else:
        form = ShopForm(instance=shop)

    return render(request, 'shop/shop_form.html', {
        "form": form,
        "shop": shop,
    })


def shop_delete(request: HttpRequest, pk: int) -> HttpResponse:

    shop = get_object_or_404(Shop, pk=pk)

# GET 요청 : 정말 삭제를 할 것인지, 한 번 더 물어봅니다.
# POST 요청 : 삭제를 하고, 다른 주소로 이동을 시킵니다.

    if request.method == "POST":
        shop.delete()  # 실제로 DB에 DELETE 쿼리 실행
        messages.success(request, f"#{pk} 포스팅을 삭제했습니다.")
        return redirect("shop:shop_list")

    return render(
        request,
        "shop/shop_confirm_delete.html",{
            "shop": shop,
        },
    )


