from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile
from django.contrib.auth import get_user_model
from .models import RecruiterProfile
from django.core.mail import send_mail
from django.conf import settings

User = get_user_model()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == "JOB_SEEKER":
            Profile.objects.create(user=instance)

        elif instance.role == "RECRUITER":
            RecruiterProfile.objects.create(user=instance)

        send_mail(
            subject="Welcome to JobHub",
            message=f"Hi {instance.first_name or instance.username},\n\n"
            "Welcome to JobHub! Your account has been created successfully.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=False,
        )
