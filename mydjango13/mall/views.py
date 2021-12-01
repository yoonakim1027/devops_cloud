from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
# 함수의 인자와 return타입에 대해서 미리미리 해두는 것이 더 안정적인 품질
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "mall/index.html")