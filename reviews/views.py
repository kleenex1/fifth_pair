from ast import Pass
from gettext import install
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, update_session_auth_hash
from .models import User


def accounts_signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accounts-login")
    else:
        form = CustomUserCreationForm()
    context = {
        'form' : form,
    }
    return render(request, "accounts/signup.html", context)


def accounts_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("test")
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, "accounts/login.html", context)

def accounts_detail(request, pk):
    form = User.objects.get(pk=pk)
    context = {
        'form' : form,
    }
    return render(request, "accounts/detail.html", context)

def test(request):
    # forms = User.objects.all()
    # context = {
    #     'forms' : forms,
    # }
    return render(request, "accounts/test.html")

def accounts_edit(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts-detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, "accounts/edit.html", context)


def accounts_password(request):
    if request.method=="POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect("accounts-detail", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, "accounts/passwd.html", context)

def accounts_logout(request):
    logout(request)
    return redirect("test")

def accounts_delete(request):
    request.user.delete()
    logout(request)
    return redirect("test")