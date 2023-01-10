from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def demo(request):
    #return HttpResponse("Hello world")
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return HttpResponse("Contact me on skype melvinmotiwa")