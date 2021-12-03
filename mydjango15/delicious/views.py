from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from delicious.forms import ShopForm
from delicious.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    qs = Shop.objects.all()
    # 항상 모든 함수를 호출하려면? 소괄호 열고닫기가 필요! .all()

    # QueryString에 query 이름의 인자를 확인
    query = request.GET.get("query", "")  # 가져온다가 아니고, 사전과 유사한 자료구조
    # .get 사전에서 가져오는데~  있다면 query를 가져오고
    # 없다면 "" 빈문자열을 반환해줘
    if query:  # 검색어가 있다면?
        qs = qs.filter(name__icontains=query)

    # template_name = "delicious/shop_list.html" #템플릿 명
    context_data = {
        "shop_list": qs,  # 값은 qs로 넘겨줄거임

    }  # 템플릿 내에서 참조할 변수 목록을 사전 형식으로
    return render(request, "delicious/shop_list.html", context_data)


# 위의 네줄의 코드는? 우리가 어떤 뷰를 작성하든지 간에 비슷함!
# 이름만 바뀌고 기본 구성이 비슷함.
# 그래서 이 함수를 호출해서 사용 가능


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = Shop.objects.get(pk=pk)  # .get()은 값을 한개를 ㅊ자아줌
    # pk=pk에서 뒤에있는 pk는 변수 명을 뜻함

    # template_name ="delicious/shop_detail.html" # detail은 이렇게 값이 고정!
    context_data = {
        "shop": shop,  # 항상 사전임!-> 변수명은 중요하지 않음. 보통은 같은 이름을 사용
    }  # 뷰마다 다름. 템플릿마다 보여주고자 하는 값을 넣어주면 돼
    return render(request, "delicious/shop_detail.html", context_data)
    # 디테일을 하려면? 프라이머리키가 어떤 값을 가진 샵을
    # 디테일을 보고자하는 모델 이름 : 모델이름_detail


def shop_new_1(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":  # 전송방식 : get/ post 방식이 있음
        # 파이썬에서는 대소문자가 상관이 있다~
        # 파이썬에서는 무조건 대문자 GET / POST
        # GET방식이면 빈 form을 보여주는 것이고, POST면 유저가 입력한 값을 받게 되는 것
        return render(request, "delicious/shop_form_1.html")
    else:  # POST
        name = request.POST['name']
        description = request.POST['description']
        address = request.POST['address']
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        telephone = request.POST['telephone']

        # post방식으로 받은 데이터기 때문에, request.POST에 우리가 html에서 입력한 값이 들어감

        # 이제 이런 값을 DB에 저장해야함
        # 저장하기에 앞서, 1차적으로 유효성 검사를 해야 함

        # TODO : 유효성 검사
        # -> latitude는 실수형이어야 함! 실수가 아니라 다른값이면 DB에서 오류남
        Shop.objects.create(
            name=name,
            description=description,
            address=address,
            latitude=latitude,
            longitude=longitude,
            telephone=telephone,

        )
        # 유효성 검사 후 , 뭐든 응답을 줘야 함  -> 잘 되었는지 아닌지 메시지라도~
        return redirect("/delicious/")  # DB에 저장을하고 delicious로 옮겨줘


# view구현 -> 가장 완벽한 형태로의 뷰 구현
shop_new = CreateView.as_view(
    model=Shop,
    form_class=ShopForm,
    success_url="/delicious/",

)