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

    company_name = models.CharField(max_length=255, blank=True)
    company_logo = models.ImageField(upload_to="company/", blank=True, null=True)
    company_description = models.TextField(blank=True)
    company_website = models.URLField(blank=True)
    company_industry = models.CharField(max_length=255, blank=True)
    company_location = models.CharField(max_length=255, blank=True)

    created = models.DateTimeField(auto_now_add=True)
