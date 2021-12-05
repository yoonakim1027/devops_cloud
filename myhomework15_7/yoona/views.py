from django.shortcuts import render

from django.views.generic import ListView, DetailView

from .models import StudyPost


# CBV로 포스트 목록 페이지 만들기

class StudyPostList(ListView):
    model = StudyPost
    ordering = '-pk' #내림차순