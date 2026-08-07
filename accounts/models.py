from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ("JOB_SEEKER", "JOB_SEEKER"),
        ("RECRUITER", "RECRUITER"),
    )
    role = models.CharField(
        max_length=20,
        choices=ROLES,
        default="JOB_SEEKER",
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class RecruiterProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)


class Company(models.Model):
    COMPANY_SIZE_CHOICES = [
        ("1-10", "1-10 Employees"),
        ("11-50", "11-50 Employees"),
        ("51-200", "51-200 Employees"),
        ("201-500", "201-500 Employees"),
        ("501-1000", "501-1000 Employees"),
        ("1000+", "1000+ Employees"),
    ]
    owner = models.OneToOneField(User, related_name="company", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=200, blank=True)
    logo = models.ImageField(upload_to="companies_logos/", null=True, blank=True)
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    founded_year = models.PositiveIntegerField(blank=True, null=True)
    company_size = models.CharField(
        max_length=20, choices=COMPANY_SIZE_CHOICES, blank=True
    )
    about = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]  # Asc order
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

