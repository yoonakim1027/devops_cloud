from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView

from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

signup = CreateView.as_view(
    # 생성을 했을 때 필요한 것은 폼
    form_class=UserCreationForm,  # 유효성검사 후 필드를 보여주는 것은 이 UserCreationForm이 알아서 함
    # 이동할 주소는 ? 이동할 주소가 필요함 !
    # 가변적으로 바뀌는 거면 클래스를 상속받아서 받아야하는데,
    # 고정이기 때문에?
    success_url=reverse_lazy('accounts:login'),
    # 프로젝트가 다 읽어와야 프로젝트가 초기화될것
    # 프로젝트가 초기화 되어야만 어떤 url이 지원되는지 알 수 있음
    # 그래야 url reverse를 알 수 있음
    # 근데 읽어오는 것보다 빨리 실행이되면? 실패함
    # 그래서 이 리버스 시간을 좀 더 늦추는 것이 필요.

    # 꼭! 우리가 직접 템플릿네임을 지정해주는 것이 좋음
    template_name="accounts/signup_form.html",
    # 디폴트가 셋팅되어야 하는 뷰가 있고,
    #
)

# login
login = LoginView.as_view(
    template_name="accounts/login_form.html",

)

# TODO : 커스텀 CBV를 만든다면, LoginRequiredMixin을 상속받도록 할 수 있습니다.
# TemplateView도 함수. 이를 장식자를 사용한 것과 같은 효과가
# login_required(TemplateView.as_view())
profile = login_required(
    TemplateView.as_view(
        # templateview는 무조건 template_name을 지정해줘야함
        template_name='accounts/profile.html',
    ))

logout = LogoutView.as_view(
    # next_page = "accounts:login"
    next_page="root",
)
