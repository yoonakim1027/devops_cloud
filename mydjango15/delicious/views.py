from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from delicious.models import Shop

def shop_list(request:HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    # 항상 모든 함수를 호출하려면? 소괄호 열고닫기가 필요! .all()

    #template_name = "delicious/shop_list.html" #템플릿 명
    context_data = {
        "shop_list": qs, #값은 qs로 넘겨줄거임

    } #템플릿 내에서 참조할 변수 목록을 사전 형식으로
    return render(request, "delicious/shop_list.html", context_data)

# 위의 네줄의 코드는? 우리가 어떤 뷰를 작성하든지 간에 비슷함!
# 이름만 바뀌고 기본 구성이 비슷함.
# 그래서 이 함수를 호출해서 사용 가능


def shop_detail(request: HttpRequest, pk:int) -> HttpResponse:
    shop =Shop.objects.get(pk=pk) # .get()은 값을 한개를 ㅊ자아줌
    # pk=pk에서 뒤에있는 pk는 변수 명을 뜻함

   # template_name ="delicious/shop_detail.html" # detail은 이렇게 값이 고정!
    context_data = {
        "shop":shop, #항상 사전임!-> 변수명은 중요하지 않음. 보통은 같은 이름을 사용
    } # 뷰마다 다름. 템플릿마다 보여주고자 하는 값을 넣어주면 돼
    return render(request, "delicious/shop_detail.html", context_data)
    # 디테일을 하려면? 프라이머리키가 어떤 값을 가진 샵을
    #디테일을 보고자하는 모델 이름 : 모델이름_detail

