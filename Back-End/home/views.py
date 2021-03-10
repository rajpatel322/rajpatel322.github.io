from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    #return HttpResponse("this is the home")
    return render(request, 'home.html')

def about(request):
    #return HttpResponse("this is the home")
    return render(request, 'index.html')
