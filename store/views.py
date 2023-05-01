from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout as user_logout
from django.contrib.auth import get_user_model
from .seed import * 
from .models import *
User = get_user_model()

# Create your views here.

def home(request):
    return render(request,'home.html')


def cart(request):
    return render(request,'cart.html')
def aboutus(request):
    return render(request,'aboutus.html') 

def shop(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 12)  # Show 25 contacts per page.

    page_number = request.GET.get("page")
    product= paginator.get_page(page_number)
    return render(request,'shop.html',{"products":product})



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



def logout(request):
    user_logout(request)
    return redirect('singin')
@login_required(login_url="singin")
def dashboard(request):
    return render(request,'dashboard.html')

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    all_products = Product.objects.all()
    popular_products = random.sample(list(all_products), 4)
    related_products=Product.objects.filter(category=product.category)
    return render(request,'detail.html',{'product':product,'popular_products':popular_products,'related_products':related_products})

def seed_data(n=22):
    product_seed()
    return HttpResponse('product Done!')