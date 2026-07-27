from django.urls import path
from .views import *

app_name = "application"

urlpatterns = [
    path("apply/<int:pk>/", apply_view, name="apply_view"),
    path(
        "job/<int:pk>/applications/", job_application_view, name="job_application_view"
    ),
    path("my-applications/", my_applications, name="my_applications"),
]
