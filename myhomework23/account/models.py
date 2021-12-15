from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.shortcuts import render


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("accouts:login")

    else:
        form = UserCreationForm()

    return render(
        request,"accounts/signup_form.html",{
            "form":form,
        }
    )