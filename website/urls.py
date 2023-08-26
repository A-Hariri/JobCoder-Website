from django.contrib import admin
from django.urls import path
from website.views import *

app_name = 'website'

urlpatterns = [
    path('', index_view, name='home'),
    path('', index_view, name='home'),
    path("JobProfile/<int:pid>/", JobProfile_view, name='JobProfile'),
    path("all_post/JobProfile/<int:pid>/", JobProfile_view, name='JobProfile'),
    path("save_value/JobProfile/<int:pid>/", JobProfile_view, name='JobProfile'),
    path("JobProfile/", JobProfile_view, name='JobProfile'),
    path("Linkedin_Blog/", Linkedin_Blog_view, name='Linkedin_Blog'),
    path('save_value/', save_value_view, name='save_value'),
    path("Jobvision_Blog/", Jobvision_Blog_view, name='Jobvision_Blog'),
    path("all_post/", all_post_view, name='all_post'),
    path('', index_view, name='home'),
    path('message', message_view, name='messages')
]
