
from django.urls import path
from employer.views import *

app_name = 'employer'

urlpatterns = [
    path('Employer_Login/', Employer_Login_view, name='Employer_Login'),
    path('Employer_Logout/', Employer_Logout_view, name='Employer_Logout'),
    path('Employer_signup/', Employer_Signup_view, name='Employer_Signup'),
    path('Advertising', Advertising_view, name='Advertising')
]


