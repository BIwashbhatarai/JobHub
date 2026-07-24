from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
