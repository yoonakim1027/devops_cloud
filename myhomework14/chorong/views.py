from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from chorong.models import ChoVideo


def index(request: HttpRequest) -> HttpResponse:
    qs = ChoVideo.objects.all()
    return render(

        request,
        "chorong/index.html", {
            "video_list": qs,
        }
    )


def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = ChoVideo.objects.get(pk=pk)

    return render(
        request,
        "chorong/video_detail.html",
        {
            "video": video,
        }, )
