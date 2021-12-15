from django.urls import path

from account import views
from blog.urls import urlpatterns

app_name = "account"

urlpatterns =[

    path('signup/',views.signup_form, name="signup_form"),
]