from django.urls import path
from .views import *

urlpatterns = [
    path("create/", create_job_view, name="create_job_view"),
    path("job-list/", job_list_view, name="job_list_view"),
    path("my-job/", my_job_view, name="my_job_view"),
    path("job-detail/<int:pk>/", job_detail_view, name="job_detail_view"),
    path("job-edit/<int:pk>/", job_edit_view, name="job_edit_view"),
    path("job-delete/<int:pk>/", job_delete_view, name="job_delete_view"),
]
