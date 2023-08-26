from django.contrib import admin
from jobseeker.models import Jobseeker,Resume,Resume_skill
# Register your models here.

admin.site.register(Jobseeker)
admin.site.register(Resume)
admin.site.register(Resume_skill)
