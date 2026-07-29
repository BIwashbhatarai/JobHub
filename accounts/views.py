from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import ProfileForm
from jobs.models import Job
from application.models import Application
from django.core.paginator import Paginator
from .forms import RecruiterProfileForm


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
            if request.user.role == "RECRUITER":
                return redirect("recruiter_dashboard_view")
            return redirect("job_seeker_dashboard_view")
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
def profile_view(request):
    if request.user.role == "JOB_SEEKER":
        profile = request.user.profile
    elif request.user.role == "RECRUITER":
        profile = request.user.recruiterprofile
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
        if request.user.role == "JOB_SEEKER":
            form = ProfileForm(
                request.POST, request.FILES, instance=request.user.profile
            )
            if form.is_valid():
                form.save()
                messages.success(
                    request,
                    "Your profile has been updated successfully",
                )
                return redirect("profile_view")
            else:
                messages.error(request, "invalid details, please try again")
        elif request.user.role == "RECRUITER":
            form = RecruiterProfileForm(
                request.POST, request.FILES, instance=request.user.recruiterprofile
            )
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
        if request.user.role == "RECRUITER":
            form = RecruiterProfileForm(instance=request.user.recruiterprofile)
        elif request.user.role == "JOB_SEEKER":
            form = ProfileForm(instance=request.user.profile)
        return render(
            request,
            "accounts/edit_profile.html",
            {"form": form},
        )


@login_required
def recruiter_dashboard_view(request):
    if request.user.role != "RECRUITER":
        messages.error(
            request,
            "Access denied. Only recruiters can access the recruiter dashboard.",
        )
        return redirect("job_seeker_dashboard_view")

    total_jobs = Job.objects.filter(
        recruiter=request.user,
    ).count()

    active_jobs = Job.objects.filter(recruiter=request.user, is_active=True).count()
    total_applicants = Application.objects.filter(job__recruiter=request.user).count()

    accepted_candidates = Application.objects.filter(
        status="ACCEPTED", job__recruiter=request.user
    ).count()

    rejected_candidates = Application.objects.filter(
        status="REJECTED", job__recruiter=request.user
    ).count()

    jobs = (
        Job.objects.filter(
            recruiter=request.user,
        )
        .prefetch_related("applications")
        .order_by("-created_at")
    )
    paginator = Paginator(jobs, 8)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)
    return render(
        request,
        "accounts/recruiter_dashboard.html",
        {
            "total_jobs": total_jobs,
            "active_jobs": active_jobs,
            "total_applicants": total_applicants,
            "jobs": jobs,
            "accepted_candidates": accepted_candidates,
            "rejected_candidates": rejected_candidates,
        },
    )


@login_required
def job_seeker_dashboard_view(request):
    if request.user.role == "RECRUITER":
        messages.error(
            request,
            "Access denied. Only recruiters can access the recruiter dashboard.",
        )
        return redirect("recruiter_dashboard_view")

    available_jobs = Job.objects.filter(is_active=True).count()
    jobs = Job.objects.filter(is_active=True).order_by("-created_at")[:6]
    total_applied_jobs = Application.objects.filter(applicant=request.user).count()
    total_pending_jobs = Application.objects.filter(
        applicant=request.user, status="PENDING,"
    ).count()
    total_accepted_jobs = Application.objects.filter(
        applicant=request.user,
        status="ACCEPTED",
    ).count()
    applied_job_ids = set(
        Application.objects.filter(applicant=request.user).values_list(
            "job_id", flat=True
        )
    )
    applications = (
        Application.objects.select_related("job")
        .filter(applicant=request.user)
        .order_by("-applied_at")[:5]
    )
    return render(
        request,
        "accounts/job_seeker_dashboard.html",
        {
            "available_jobs": available_jobs,
            "total_applied_jobs": total_applied_jobs,
            "applications": applications,
            "jobs": jobs,
            "applied_job_ids": applied_job_ids,
            "total_pending_jobs": total_pending_jobs,
            "total_accepted_jobs": total_accepted_jobs,
        },
    )
