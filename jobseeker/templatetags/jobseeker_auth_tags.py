from django import template
from django.contrib.auth import get_user
from jobseeker.backends import JobSeekerBackend

register = template.Library()



@register.filter(name='jobseeker_is_authenticated')
def jobseeker_is_authenticated(request):
    user = get_user(request)
    return user.is_authenticated


@register.filter(name='jobseeker_name')
def jobseeker_name(request):
    user = get_user(request)
    return user