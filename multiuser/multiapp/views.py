from lib2to3.fixes.fix_input import context

from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect

from multiapp.models import CustomUser

from multiapp.forms import Customusercreationform


# Create your views here.
def home(request):
    return render(request,"home.html")

def stu_home(request):
    return render(request,"stuhome.html")

def teach_home(request):
    return render(request,"teachhome.html")

def register(request):
    if request.method=="POST":
        u=request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        e = request.POST['e']
        f = request.POST['f']
        l = request.POST['l']
        ph = request.POST['ph']
        g=request.POST['g']
        r=request.POST.get('r')

        if p==cp:
            u=CustomUser.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l,phone=ph,gender=g,role=r)
            u.save()
            return redirect('home')
        else:
            messages.error(request,"Passwords are not same")

    return render(request,"register.html")

def register1(request):
    if request.method=="POST":
        form=Customusercreationform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=Customusercreationform()
    context={'form':form}
    return render(request,"register1.html",context)


def user_login(request):
    if request.method=="POST":
        u=request.POST['u']
        p=request.POST['p']
        user=authenticate(username=u,password=p)
        if user and user.role=="student":
            login(request,user)
            return redirect('stuhome')
        elif user and user.role=="teacher":
            login(request,user)
            return redirect('teachhome')
        else:
            messages.error(request,"Invalid user credentials")
    return render(request,"login.html")