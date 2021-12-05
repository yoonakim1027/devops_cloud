from django.shortcuts import render
from django.views.generic import ListView, DetailView
# CBV 로 목록 페이지 만들기
from yoona.models import StudyPost


class StudyPostList(ListView):
    model = StudyPost
    ordering = '-pk'



class

