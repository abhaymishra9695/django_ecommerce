from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

def home(request):
    return render(request,'home.html')


def cart(request):
    return render(request,'cart.html')
def aboutus(request):
    return render(request,'aboutus.html') 

def shop(request):
    return render(request,'shop.html')


def contectus(request):
    return render(request,'contectus.html')
   

def checkout(request):
    return render(request,'checkout.html')


def singup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        user=User.objects.create(name=name,email=email)
        user.set_password(password)
        user.save()
        return redirect('singin')
    return render(request,'singup.html')
    

def singin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
    return render(request,'singin.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    return render(request,'dashboard.html')
    