from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse("this is the home")
    return render(request, 'home.html')


def project(request):
    # return HttpResponse("this is the home")
    return render(request, 'project.html')


def contact(request):
    # return HttpResponse("this is the home")
    return render(request, 'contact.html')
