from django.shortcuts import render, get_object_or_404

from django.http import HttpRequest, HttpResponse
from shop.models import Shop, Category, Tag


def shop_list(request:HttpRequest)-> HttpResponse:
    qs = Shop.objects.all()
    return render(request, "shop/shop_list.html",{
        "shop_list":qs,
    })


def shop_detail(request:HttpRequest, pk:int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    return render(request, "shop/shop_detail.html",{
        "shop": shop,

    })

