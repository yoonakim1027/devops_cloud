from . import views
from django.urls import path

app_name = 'diary'

urlpatterns = [
    path("", views.post_list, name='post_list'),
]
