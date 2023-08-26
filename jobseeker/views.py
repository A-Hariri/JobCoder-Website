from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from jobseeker.models import Resume_skill,Resume,Jobseeker
from website.models import Skills
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect



# Create your views here.


# @csrf_protect
def JobSeeker_Login_view(request):

    if request.method == 'POST':
        number = request.POST['number']
        password = request.POST['password']
        print(number)
        print(password)
        user = authenticate(request, number=number, password=password)

        if user is not None:
            # print("yes")
            login(request, user)
            return redirect("/")

        else:
            # print("no")
            return render(request,'jobseeker/JobSeeker_Login.html')


    return render(request, 'jobseeker/JobSeeker_Login.html')



@login_required
def JobSeeker_logout_view(request):
    logout(request)
    return redirect("/")



@csrf_protect
def JobSeeker_Signup_view(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        surename = request.POST.get('surename')
        number = request.POST.get('number')
        password = request.POST.get('password')
        print(name,surename,number,password)
        Jobseeker.objects.create(name=name, surename=surename,
                                 number=number, password=password)

    # jobseeker=Jobseeker.objects.all()
    return render(request, 'jobseeker/JobSeeker_Login.html')



@csrf_exempt
def Resume_view(request):


    if request.method == 'POST' and 'resume' in request.FILES:
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        birthdate = request.POST.get('birthdate')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        gender = request.POST.get('gender')
        marital_status = request.POST.get('marital-status')
        Favoritefield = request.POST.get('Favoritefield')
        field = request.POST.get('field')
        university = request.POST.get('university')
        degree = request.POST.get('degree')
        start_year = request.POST.get('start-year')
        end_year = request.POST.get('end-year')
        Workplace = request.POST.get('Workplace')
        mager = request.POST.get('mager')
        position = request.POST.get('position')
        duration = request.POST.get('duration')
        resume = request.FILES['resume']


        abilities = request.POST.getlist('abilities')

        new_resume = Resume.objects.create(name=name,surname=surname,birthdate=birthdate,
                                           location=location,email=email,phone=phone,
                                           gender=gender,marital_status=marital_status,
                                           Favoritfield=Favoritefield,field=field,
                                        university=university,degree=degree,start_year=start_year,
                                        end_year=end_year,Workplace=Workplace,mager=mager,position=position,
                                        duration=duration,resume=resume)



        abilities = abilities[0].split('\r\n')
        print(abilities)
        for skill_name in abilities:


            skill, created = Skills.objects.get_or_create(name=skill_name)

            Resume_skill.objects.create(skill=skill, resume=new_resume)



    skills = Skills.objects.all()


    return render(request, 'jobseeker/Resume.html', {'skills': skills})



