from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProfileForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has successfully created, please log in now"
            )
            return redirect("login_view")
        else:
            messages.error(request, "Invalid details, please try again")
    else:
        form = RegistrationForm()
    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have successfully logged in ")
            return redirect("dashboard_view")
        else:
            messages.error(request, "Please enter a correct username and password.")
    else:
        form = LoginForm()
    return render(
        request,
        "accounts/login.html",
        {"form": form},
    )


@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect("login_view")


@login_required
def dashboard_view(request):
    return render(request, "accounts/dashboard.html")


@login_required
def profile_view(request):
    profile = request.user.profile
    return render(
        request,
        "accounts/profile.html",
        {
            "profile": profile,
        },
    )


@login_required
def edit_profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your profile has been updated successfully",
            )
            return redirect("profile_view")
        else:
            messages.error(request, "invalid details, please try again")
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(
        request,
        "accounts/edit_profile.html",
        {"form": form},
    )
