# CBV 방식으로 구현
from django.views.generic import ListView

# class명.view()
from shop.models import Shop, Category


# ListView를 상속받음
class ShopListView(ListView):
    model = Shop

    # 원래 이 함수는 모든 클래스 기반 뷰에 다 존재함
    # 템플릿에서 사용할 변수목록(사전)을 만들어주는 함수
    def get_context_data(self, **kwargs):
        # 부모가 인자를 받은데로, 자식이 재구현
        # 밑의 context_data는 사전
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = Category.objects.all()
        return context_data

# 여러 줄 쓸 때에는 보통 콤마를 마지막에 씀.
# 동작에는 영향은 없음

shop_list = ShopListView.as_view(
    model=Shop,
    # 리스트 뷰에서 필수적인 속성은 모델 !
    # 다른 것들은 다 옵션임 - > 안쓰면 적용될 디폴트 값이 존재하다는 뜻
    template_name="shop/shop_list.html"

)
