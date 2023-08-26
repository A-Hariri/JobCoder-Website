from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core.paginator import Paginator


from website.models import JobPost,Message


def index_view(request):
    posts = JobPost.objects.order_by('creat_date')[1:5]
    context = {'posts': posts}
    return render(request, 'website/Index.html', context)


def JobProfile_view(request,pid):
    post =JobPost.objects.get(pk=pid)
    # post = JobPost.objects.all(pk = pid)

    context = {'post': post}
    return render(request, 'website/JobProfile.html',context)


def Linkedin_Blog_view(request):
    return render(request, 'website/Linkedin_Blog.html')

def Jobvision_Blog_view(request):
    return render(request, 'website/Jobvision_Blog.html')

def all_post_view(request):
    posts = JobPost.objects.all()
    posts = Paginator(posts, 2)
    page_number = request.GET.get('page')
    posts = posts.get_page(page_number)
    context = {'posts': posts}
    return render(request, 'website/all_post.html', context)


def save_value_view(request):


    if request.method == 'POST':
        selected_city = request.POST.get('selected_city')
        selected_job = request.POST.get('selected_job')
        posts = JobPost.objects.all()
        posts = posts.filter(city=selected_city,category=selected_job)
        context = {'posts': posts}
        print(selected_job)
        print(selected_city)
    return render(request, 'website/all_post.html', context)




@ensure_csrf_cookie
def message_view(request):

    if request.method == 'POST':
        print("yes")
        contact_email = request.POST.get('contact-email')
        message = request.POST.get('message')

        Message.objects.create(contact_email=contact_email, message=message)



    return render(request, 'website/Index.html')