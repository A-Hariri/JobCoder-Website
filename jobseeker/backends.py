from django.contrib.auth.backends import BaseBackend
from .models import Jobseeker


class JobSeekerBackend(BaseBackend):
    def authenticate(self, request, number=None, password=None):
       try:
            user = Jobseeker.objects.get(number=number)
            if user.password == password:
                return user
       except Jobseeker.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Jobseeker.objects.get(pk=user_id)
        except Jobseeker.DoesNotExist:
            return None