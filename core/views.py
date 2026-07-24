from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated:
        return redirect("dashboard_view")

    return render(
        request,
        "core/home.html",
    )
