from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from django.views.generic import TemplateView, DetailView, ListView, CreateView, UpdateView

from app1.models import Menu,MenuItem



# Create your views here.
class Display(TemplateView):
    template_name = 'base.html'



class Detail(DetailView):
    template_name = 'items.html'
    model = Menu
    context_object_name = 'item'


class List(ListView):
    template_name = 'home.html'
    model = Menu
    context_object_name = 'menu'





class Add(CreateView):
    model = MenuItem
    fields = ['name','price','is_vegetarian','menu']
    template_name = 'add.html'
    success_url = reverse_lazy('home')



class Update(UpdateView):
    template_name = 'update.html'
    fields= ['name','price','is_vegetarian','menu']
    model=MenuItem
    success_url=reverse_lazy('home')

