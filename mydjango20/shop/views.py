from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# 새로운 Shop 등록 페이지
# 바뀌는 인자가 없기 때문에, pk를 안받아도 돼
# /shop/new/
from shop.form import ShopForm
from shop.models import Shop


def shop_new(request: HttpRequest) -> HttpResponse:
    # raise NotImplementedError('곧 구현 예정') # 예외를 발생시키는 raise

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            # shop 디테일 규를 구현했다면 ?
            return redirect("shop:shop_detail", saved_post.pk)


    else:
        form = ShopForm()
    return render(request, "shop/shop_form.html", {
        "form": form,  # 빈 서식 만들기
    })


# /shop/100/
def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop,pk=pk)
    return render(request,"shop/shop_detail.html",{
        "shop":shop, #shop이름으로 shop을 구현
    })
