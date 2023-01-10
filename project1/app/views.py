from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Place,Services,Teams
# Create your views here.
def home(request):
    obj=Place.objects.all()
    services=Services.objects.all()
    teams=Teams.objects.all()
    return render(request,"index.html",{'result':obj,'service':services,'teams':teams})

def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        upass=request.POST['upass']
        user=auth.authenticate(username=uname,password=upass)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        uname=request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        if pass1==pass2:
            if User.objects.filter(username=uname).exists():
                messages.info(request, "Username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken!')
                return redirect('register')
            else:
                user=User.objects.create_user(username=uname,email=email,first_name=fname,last_name=lname,password=pass1)
                user.save();
                print("user registered")
                return redirect('login')
        else:
            messages.info(request,'Password not Matching!')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def contact(request):
    name = "Melvin"
    return render(request,"contact.html",{'obj':name})
def details(request):
    return render(request,"details.html")
def thanks(request):
    return HttpResponse("Thank You!")

def calculate(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    add=x+y
    sub=x-y
    div=x%y
    mul=x*y
    return render(request,"result.html",{'add':add,'x':x,'y':y,'sub':sub,'div':div,'mul':mul})
