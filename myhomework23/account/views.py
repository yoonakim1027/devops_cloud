from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.shortcuts import render, redirect


def signup_form(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("account:signup_form")

    else:
        form = UserCreationForm()

    return render(
        request,"accounts/signup_form.html",{
            "form":form,
        }
    )