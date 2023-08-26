from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _



# Create your models here.
class Skills(models.Model):
    name =models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Options(models.Model):
    name =models.CharField(max_length=255)

    def __str__(self):
        return self.name


# class Collaboration(models.TextChoices):
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name



class JobPost(models.Model):
    image = models.ImageField(upload_to='JobPost/', default='JobPost/default.svg')
    title = models.CharField(max_length=50)
    company_name = models.CharField(max_length=100)
    address = models.TextField(max_length=500)
    day = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    skills = models.ManyToManyField(Skills)
    options = models.ManyToManyField(Options)
    cooperation = models.CharField(max_length=20,default='تمام وقت')
    city = models.CharField(max_length=50,default='تهران')
    gender = models.CharField(max_length=20,default='مهم نیست')
    category = models.CharField(max_length=20,default='هوش مصنوعی و داده')
    salary = models.CharField(max_length=20,default='توافقی')
    experience = models.CharField(max_length=15,default='مهم نیست')
    creat_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class JobPost_Option(models.Model):
    option = models.ForeignKey(Options, on_delete= models.CASCADE,null=True)
    jobPost = models.ForeignKey(JobPost, on_delete= models.CASCADE,null=True)



    def __str__(self):
        return "{option}_{jobPost}".format(option=self.option, jobPost=self.JobPost)




class jobPost_skill(models.Model):
    skill= models.ForeignKey(Skills, on_delete= models.CASCADE,null=True)
    jobPost = models.ForeignKey(JobPost, on_delete= models.CASCADE,null=True)


    def __str__(self):
        return "{jobPost}_{skill}".format(jobPost=self.jobPost, skill=self.skill)




class Message(models.Model):
    message = models.TextField(max_length=1000)
    contact_email = models.EmailField(max_length=200)

    def __str__(self):
        return "{contact_email}".format(contact_email=self.contact_email)



