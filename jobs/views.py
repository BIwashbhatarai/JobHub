from django.shortcuts import render, redirect, get_object_or_404
from .forms import JobForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Job
from django.utils import timezone
from application.models import Application
from django.db.models import Q
from django.core.paginator import Paginator


@login_required
def create_job_view(request):
    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()
            messages.success(request, "Job created successfully.")
            return redirect("jobs:job_list_view")

        messages.error(
            request,
            "Job could not be created. Please check the form and try again.",
        )
    else:
        form = JobForm()
    return render(
        request,
        "jobs/create_job.html",
        {"form": form},
    )


@login_required
def job_list_view(request):
    search = request.GET.get("q")
    job_type = request.GET.get("job_type")
    experience = request.GET.get("experience")
    sort = request.GET.get("sort")

    jobs = Job.objects.filter(
        is_active=True,
        application_deadline__gte=timezone.now().date(),
    ).order_by("-created_at")

    if search:
        jobs = jobs.filter(
            Q(title__icontains=search)
            | Q(company_name__icontains=search)
            | Q(location__icontains=search)
        )

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    if experience:
        jobs = jobs.filter(experience_level=experience)

    if sort:
        if sort == "oldest":
            jobs = jobs.order_by("created_at")
        elif sort == "newest":
            jobs = jobs.order_by("-created_at")
        elif sort == "salary_low":
            jobs = jobs.order_by("salary")
        elif sort == "salary_high":
            jobs = jobs.order_by("-salary")

    paginator = Paginator(jobs, 8)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)

    return render(
        request,
        "jobs/job_list.html",
        {
            "jobs": jobs,
        },
    )


@login_required
def job_detail_view(request, pk):
    job = get_object_or_404(Job, pk=pk)
    applied = Application.objects.filter(
        applicant=request.user,
        job=job,
    ).exists()

    return render(
        request,
        "jobs/job_details.html",
        {
            "job": job,
            "applied": applied,
        },
    )


@login_required
def my_job_view(request):
    jobs = Job.objects.filter(
        recruiter=request.user,
    )

    paginator = Paginator(jobs, 8)
    page_number = request.GET.get("page")
    jobs = paginator.get_page(page_number)
    return render(
        request,
        "jobs/my_job.html",
        {"jobs": jobs},
    )


@login_required
def job_edit_view(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)

    if request.method == "POST":
        form = JobForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Job updated successfully",
            )
            return redirect("jobs:my_job_view")
        else:
            messages.success(
                request,
                "Unable to update the job. Please try again.",
            )
    else:
        form = JobForm(instance=job)
    return render(
        request,
        "jobs/edit_job.html",
        {"form": form},
    )


@login_required
def job_delete_view(request, pk):
    job = get_object_or_404(Job, pk=pk, recruiter=request.user)
    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully")
        return redirect("jobs:my_job_view")
    return render(
        request,
        "jobs/delete_job.html",
        {"job": job},
    )
