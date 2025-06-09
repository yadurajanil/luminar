from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from users.models import CustomUser


# Create your views here.
def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user:
            login(request,user)
            return redirect('books:home')
        else:
            messages.error(request,"Invalid user credentials")
    return render(request,"login.html")

def register(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        cp=request.POST['cp']
        e=request.POST['e']
        f=request.POST['f']
        l=request.POST['l']
        ph=request.POST['ph']
        ad=request.POST['a']
        if p==cp:
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,phone=ph,address=ad)
            u.save()
            return redirect('books:home')
        else:
            messages.error(request,"Passwords are not same")

    return render(request,"register.html")

@login_required
def user_logout(request):
    logout(request)
    return redirect('users:login')