from django.shortcuts import render

from django.http import HttpRequest, HttpResponse
from shop.models import Shop, Category, Tag


def shop_list(request:HttpRequest)-> HttpResponse:
    qs = Shop.objects.all()
    return render(request, "shop/shop_list.html",{
        "shop_list":qs,
    })


