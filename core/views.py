from django.shortcuts import render, redirect


def home(request):
    if request.user.is_authenticated and request.user.role == "RECRUITER":
        return redirect("recruiter_dashboard_view")

    if request.user.is_authenticated and request.user.role == "JOB_SEEKER":
        return redirect("job_seeker_dashboard_view")

    return render(
        request,
        "core/home.html",
    )
