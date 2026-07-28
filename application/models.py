from django.db import models
from jobs.models import Job
from django.contrib.auth import get_user_model

User = get_user_model()


class Application(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("ACCEPTED", "Accepted"),
        ("REJECTED", "Rejected"),
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="applications",
    )

    resume = models.FileField(
        upload_to="resume/",
        blank=True,
        null=True,
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PENDING",
    )

    cover_letter = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("applicant", "job")

    def __str__(self):
        return f"{self.applicant.username} applied for {self.job.title}"
