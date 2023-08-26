from django.contrib import admin
from website.models import JobPost, Skills, Options,Message

# Register your models here.
@admin.register(JobPost)
@admin.register(Skills)
@admin.register(Options)
@admin.register(Message)
class JobPostAdmin(admin.ModelAdmin):
    pass



# admin.site.register(JobPost,JobPostAdmin)
