from django import template
from django.contrib.auth import get_user
from jobseeker.models import Jobseeker
from django.shortcuts import render
from website.models import JobPost


register = template.Library()

@register.filter(name='detect_model')
def detect_model(request):
    user_app = 'Jobseeker' if isinstance(request.user, Jobseeker) else 'Employer'
    print("**********",user_app)
    # context = {'user_app': user_app}
    # print("(((((((((((((((((((",context)
    return user_app

# @register.inclusion_tag('')


