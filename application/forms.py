from django import forms
from .models import Application


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ["resume", "cover_letter"]

        widgets = {
            "cover_letter": forms.Textarea(
                attrs={
                    "rows": 8,
                    "placeholder": "Write a short cover letter explaining why you're a good fit for this position...",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
