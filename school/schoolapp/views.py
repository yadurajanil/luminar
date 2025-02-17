from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template.context_processors import request

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView,View

from schoolapp.models import School,Student

from schoolapp.forms import Schoolform



# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class Addschool(CreateView):
    model = School
    template_name = "addschool.html"
    # fields = ['name','principal','location']
    form_class = Schoolform
    success_url = reverse_lazy('home')

class Addstudent(CreateView):
    model = Student
    template_name = "addstudent.html"
    fields = ['name','age','school']
    success_url = reverse_lazy('home')

class Schoollist(ListView):
    model=School
    template_name="schoollist.html"
    context_object_name="school"

class Schooldetail(DetailView):
    model=School
    template_name = "detail.html"
    context_object_name = "school"

class Studentdetail(ListView):
    model=Student
    template_name = "studetail.html"
    context_object_name = "student"

class Register(CreateView):
    model=User
    fields=['username','password','email','first_name','last_name']
    template_name = 'register.html'
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        u=form.cleaned_data['username']
        p=form.cleaned_data['password']
        e=form.cleaned_data['email']
        f=form.cleaned_data['first_name']
        l=form.cleaned_data['last_name']

        u=User.objects.create_user(username=u,password=p,email=e,first_name=f,last_name=l)
        u.save()
        return redirect('home')

class Login(LoginView):
    template_name = 'login.html'

class Logout(View):
    def get(self,request):
        logout(request)
        return redirect('home')