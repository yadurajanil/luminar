from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from shop.models import Category
from shop.models import Product

from django.contrib.auth.models import User

class Home(ListView):
    model=Category
    context_object_name ='key'
    template_name="category.html"


class CategoryDetails(DetailView):
    model=Category
    template_name="categorydetails.html"
    context_object_name="k"


class ProductDetails(DetailView):
    model = Product
    template_name = 'productdetails.html'
    context_object_name = 'n'

def register(request):
    if(request.method=="POST"):
        u=request.POST['u']
        p = request.POST['p']
        p1 = request.POST['p1']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        if(p==p1):
            u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
            u.save()
            return redirect('shop:home')
        else:
            return HttpResponse('password are not the same')
    return render(request,'register.html')


def user_login(request):
    if request.method== "POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request, user)
            return redirect('shop:home')
        else:
            messages.error(request,"Invalid User Credentials")
    return render(request,'login.html')


def user_logout(request):
    logout(request)
    return redirect('shop:home')

class Add_cart(CreateView):
    model = Category
    fields = ['name','desc','image']
    template_name = 'addcategory.html'
    success_url = reverse_lazy('shop:home')

class Add_pro(CreateView):
    model = Product
    fields = ['name', 'desc', 'image','price','stock','category']
    template_name = 'addpro.html'
    success_url = reverse_lazy('shop:home')




