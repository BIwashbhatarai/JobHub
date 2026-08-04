from .models import Application
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=Application)
def send_application_confirmation_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Application Submitted Successfully",
            message=f"""Hi {instance.applicant.first_name or instance.applicant.username},

        Your application for the position of "{instance.job.title}" at {instance.job.company_name} has been submitted successfully.

        The recruiter will review your application, and if you are shortlisted, they may contact you for the next steps.

        You can track your application status by logging into your JobHub account.

        Thank you for using JobHub, and we wish you the best of luck!

        Best regards,
        The JobHub Team
        """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.applicant.email],
            fail_silently=False,
        )


@receiver(post_save, sender=Application)
def notify_recruiter_new_application(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="Application Submitted Successfully",
            message=f"""Hi {instance.job.recruiter.username},
            A new candidate has applied for your job posting
            "Python Django Intern".

             Candidate: {instance.applicant.username}
             
            """,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.job.recruiter.email],
            fail_silently=False,
        )
