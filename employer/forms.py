from django import forms
from website.models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['options']