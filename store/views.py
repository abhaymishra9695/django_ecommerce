from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,logout

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
    return render(request,'singup.html')
    

def singin(request):
    return render(request,'singin.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def dashboard(request):
    return render(request,'dashboard.html')
    