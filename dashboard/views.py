from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import * 
from django.contrib.auth import login,authenticate
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')
def loginpage(request):
    return render(request,'authentication-login.html')
def register(request):
    return render(request,'authentication-register.html')
def discountcode(request):
    return render(request,'discount-code.html')
def docs(request):
    return render(request,'docs.html')
def icontabler(request):
    return render(request,'icon-tabler.html')
def samplepage(request):
    return render(request,'sample-page.html')
def alerts(request):
    return render(request,'ui-alerts.html')
def buttons(request):
    return render(request,'ui-buttons.html')
def card(request):
    return render(request,'ui-card.html')
def forms(request):
    return render(request,'ui-forms.html')
def typography(request):
    return render(request,'ui-typography.html')

def registersave(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        print(username,email,password)
        Customuser.objects.create_user(username=username,name=username,email=email,password=password)
        return redirect('admindashboard:login')
def loginsave(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('paintapp:index')
        else:
            messages.error(request,'incorrect password')
            return redirect('admindashboard:login')
        
        
