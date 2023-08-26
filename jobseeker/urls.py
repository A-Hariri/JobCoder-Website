from django.urls import path
from jobseeker.views import *

app_name = 'jobseeker'

urlpatterns = [
    path('JobSeeker_Login/', JobSeeker_Login_view, name='JobSeeker_Login'),
    path('JobSeeker_Logout/', JobSeeker_logout_view, name='JobSeeker_Logout'),
    path('JobSeeker_signup/', JobSeeker_Signup_view, name='JobSeeker_signup'),
    path('Resume/', Resume_view, name='Resume')
]
