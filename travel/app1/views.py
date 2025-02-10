from django.shortcuts import render
from app1.models import Place,Team

def home(request):
    p=Place.objects.all()
    t=Team.objects.all()
    context={'p':p,'t':t}
    return render(request,'home.html',context)


def about(request):
    return render(request,'about.html' )

