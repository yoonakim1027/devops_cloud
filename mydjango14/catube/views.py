from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def index(request: HttpRequest) -> HttpResponse:
    return render(request, "catube/index.html")
# return render(request, 앱이름 한번 써주고 / 생성할 html


