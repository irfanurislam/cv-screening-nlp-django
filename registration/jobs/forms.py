# jobs/forms.py
from django import forms
from .models import Candidate

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['job_title', 'job_position', 'company_email', 'phone_number', 'skills', 'job_description']
