from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from website.models import Skills,Options,JobPost,jobPost_skill,JobPost_Option
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from .models import Employer

from .backends import EmployerBackend

# Create your views here.

def Employer_Login_view(request):
    if request.method == 'POST':


        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email_employer=email, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(request, 'employer/Employer_login.html')


    return render(request, 'employer/Employer_login.html')

@login_required
def Employer_Logout_view(request):
    logout(request)
    return redirect("/")

@csrf_protect
def Employer_Signup_view(request):
    if request.method == 'POST':

        company_name = request.POST.get('company-name')
        email_employer = request.POST.get('email')
        password = request.POST.get('password')


        Employer.objects.create(company_name=company_name, email_employer=email_employer,
                                 password=password)

    # jobseeker=Jobseeker.objects.all()
    return render(request, 'employer/Employer_Login.html')




@csrf_exempt
def Advertising_view(request):
    if request.method == 'POST' and 'image' in request.FILES:

        image = request.FILES['image']
        title = request.POST.get('title')
        company_name = request.POST.get('category')
        address = request.POST.get('address')
        day = request.POST.get("time_day")
        description = request.POST.get('description')
        cooperation = request.POST.get('cooperation')
        city = request.POST.get('city')
        gender = request.POST.get('gender')
        category = request.POST.get('category')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')

        skills = request.POST.getlist('suggestions')
        options = request.POST.getlist('options')

        new_resume = JobPost.objects.create(image=image, title=title, company_name=company_name,
                                            address=address, day=day, description=description,
                                            cooperation=cooperation, city=city, gender=gender,
                                            category=category, salary=salary, experience=experience)

        skills = skills[0].split('\r\n')
        options = options[0].split('\r\n')

        for options_name in options:
            option, created = Options.objects.get_or_create(name=options_name)
            JobPost_Option.objects.create(option=option, jobPost=new_resume)

        for skill_name in skills:
            skill, created = Skills.objects.get_or_create(name=skill_name)
            jobPost_skill.objects.create(jobPost=new_resume, skill=skill)

    skills = Skills.objects.all()
    return render(request, 'employer/Advertising.html', {'skills': skills})
