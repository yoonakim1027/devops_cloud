from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import StudyPost


# 이번에 내가 만들 페이지 목록  (3개)
# 1. 대문 페이지
# 2. 블로그 페이지
# 3. 자기소개 페이지

# CBV 방식으로 페이지 만들기

# list 페이지
class StudyPostList(ListView):
    model = StudyPost


# detail 페이지
class StudyPostDetail(DetailView):
    model = StudyPost
