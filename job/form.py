from django import forms
from .models import JobResponse


class ResponseForm(forms.ModelForm):
    class Meta:
        model = JobResponse
        fields = ('job_application', 'name', 'surname', 'number', 'email')


