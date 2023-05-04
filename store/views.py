from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout as user_logout
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from .seed import * 
from .models import *
from django.db.models import  Q
User = get_user_model()

# Create your views here.

def home(request):
    return render(request,'home.html')


def cart(request):   # sourcery skip: remove-unreachable-code
    cart=Cart.objects.filter(is_paid=False,user=request.user).first()
    cart_items = cart.cart_items.all()
  
    # return HttpResponse(total_price)
    return render(request,'cart.html',{"cart":cart,"cart_items":cart_items})
def aboutus(request):
    return render(request,'aboutus.html') 

def shop(request):  # sourcery skip: merge-comparisons, merge-duplicate-blocks, remove-pass-body, remove-redundant-if, remove-unreachable-code
   
    product_sorting=request.GET.get("productsorting")
    if product_sorting=="date":
        product_list=Product.objects.all().order_by('date_joined')
    elif product_sorting=="price":
         product_list=Product.objects.all().order_by('regular_price')
    elif product_sorting=="price-desc":
        product_list=Product.objects.all().order_by('-regular_price')
    elif product_sorting=="menu_order":
        product_list=Product.objects.all()
    else:
        product_list=Product.objects.all()
    
    post_per_page=request.GET.get("post_per_page")
    if post_per_page=="12":
        post_per_page=12
    elif post_per_page=="16":
        post_per_page=16
    elif post_per_page=="18":
        post_per_page=18
    elif post_per_page=="21":
        post_per_page=21
    elif post_per_page=="24":
        post_per_page=24
    elif post_per_page=="30":
        post_per_page=30
    else :
        post_per_page=12

    catageries=Category.objects.all()

    paginator = Paginator(product_list, post_per_page)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    product= paginator.get_page(page_number)
    return render(request,'shop.html',{"products":product,"catageries":catageries})



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


def add_cart_product(request,slug):
    product=Product.objects.get(slug=slug)
    user=request.user
    cart,_=Cart.objects.get_or_create(user=user,is_paid=False)
    cartitem=CartItem.objects.create(cart=cart,product=product) 
    cartitem.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def remove_cart_product(request,cart_item_id): 
    # return HttpResponse(cart_item_id)
    try:
        cartitem=CartItem.objects.filter(id=cart_item_id) 
        cartitem.delete()
    except Exception as e:
        print(e)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 
def seed_data(request):

    product_seed()
    return HttpResponse("done")




def increment_cart(request,cart_item_id):  # sourcery skip: last-if-guard, remove-unreachable-code
       
        cart_item = CartItem.objects.get(id=cart_item_id)
        cart_item.quantity = cart_item.quantity+1
        cart_item.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     

def decrement_cart(request,cart_item_id):  # sourcery skip: last-if-guard, remove-unreachable-code
        
        cart_item = CartItem.objects.get(id=cart_item_id)
        if cart_item.quantity>1:
            cart_item.quantity = cart_item.quantity-1
            cart_item.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     

        else:
            cart_item.delete()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     


def delete_cart(request):
    cart_item = CartItem.objects.all()
    cart_item.delete()    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER')) 


def catagory_by_product(request,slug):
    product_sorting=request.GET.get("productsorting")
    if product_sorting=="date":
        product_list=Product.objects.all().order_by('date_joined')
    elif product_sorting=="price":
         product_list=Product.objects.all().order_by('regular_price')
    elif product_sorting=="price-desc":
        product_list=Product.objects.all().order_by('-regular_price')
    elif product_sorting=="menu_order":
        product_list=Product.objects.all()
    else:
       product_list=Product.objects.all()
    post_per_page=request.GET.get("post_per_page")
    if post_per_page=="12":
        post_per_page=12
    elif post_per_page=="16":
        post_per_page=16
    elif post_per_page=="18":
        post_per_page=18
    elif post_per_page=="21":
        post_per_page=21
    elif post_per_page=="24":
        post_per_page=24
    elif post_per_page=="30":
        post_per_page=30
    else :
        post_per_page=12
    
    catageries=Category.objects.all()
    product_list=Product.objects.filter(category__slug=slug)
    paginator = Paginator(product_list, post_per_page)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    product= paginator.get_page(page_number)
    return render(request,'shop.html',{"products":product,"catageries":catageries})


def search(request):
    catageries=Category.objects.all()
    search=request.GET.get("search")
    product=Product.objects.filter(name__icontains=search)
    return render(request,'shop.html',{"products":product,"catageries":catageries})

def Categories(request):
    Categories=Category.objects.all()
    paginator = Paginator(Categories, 5)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    Categories= paginator.get_page(page_number)
    return render(request,'categories.html',{"Categories":Categories})

def addcategories(request):
    if request.method=="POST":
        catagery=  request.POST.get('catagery')
        slug= slugify(catagery)
        catagery=Category.objects.create(name=catagery,slug=slug) 
        catagery.save()
    return render(request,'addcategory.html')

def update_category(request,slug):
    catagery=Category.objects.get(slug=slug)
    if request.method=="POST":
        name=  request.POST.get('catagery')
        slug= slugify(name)
        catagery.name=name
        catagery.slug=slug
        catagery.save()
        return redirect('Categories')
    return render(request,'editcategory.html',{"catagery":catagery})

def delete_category(request,slug):
    catagery=Category.objects.get(slug=slug)
    catagery.delete()
    return redirect('Categories')

def product(request):
    product_list=Product.objects.all()
    paginator = Paginator(product_list, 10)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    product= paginator.get_page(page_number)
    return render(request,'product.html',{"products":product})

def add_product(request):
    if request.method=="POST":
        catagery=  request.POST.get('catagery')
        slug= slugify(catagery)
        catagery=Category.objects.create(name=catagery,slug=slug) 
        catagery.save()
    return render(request,'add_product.html')