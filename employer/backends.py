from django.contrib.auth.backends import BaseBackend
from .models import Employer


class EmployerBackend(BaseBackend):
    def authenticate(self, request, email_employer=None, password=None):
       try:
            user = Employer.objects.get(email_employer=email_employer)
            if user.password == password:
                return user
       except Employer.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Employer.objects.get(pk=user_id)
        except Employer.DoesNotExist:
            return None