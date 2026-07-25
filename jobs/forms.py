from .models import Job
from django import forms


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            "title",
            "company_name",
            "location",
            "description",
            "requirements",
            "salary",
            "job_type",
            "experience_level",
            "application_deadline",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
