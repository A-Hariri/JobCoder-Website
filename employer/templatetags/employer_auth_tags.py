from django import template
from django.contrib.auth import get_user
from employer.backends import EmployerBackend

register = template.Library()



@register.filter(name='employer_is_authenticated')
def employer_is_authenticated(request):
    user = get_user(request)
    return user.is_authenticated


@register.filter(name='employer_name')
def employer_name(request):
    user = get_user(request)
    return user


