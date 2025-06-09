from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from movieapp.models import Movie




# Create your views here.
# def home(request):
#     m=Movie.objects.all()
#     context={'movie':m}
#     return render(request,'home.html',context)


from django.views.generic import ListView, CreateView, DetailView, UpdateView,DeleteView


class Home(ListView):
    model=Movie
    template_name="home.html"
    context_object_name="movie"

# def addmovie(request):
#     if(request.method=="POST"):
#         tit=request.POST['t']
#         des=request.POST['d']
#         lan=request.POST['l']
#         yea=request.POST['y']
#         img=request.FILES['i']
#         m=Movie.objects.create(title=tit,description=des,language=lan,year=yea,image=img)
#         m.save()
#
#         return redirect('home')
#
#     return render(request,'addmovie.html')


class Addmovie(CreateView):
    template_name='add1.html'
    fields=['title','description','year','language','image']
    model=Movie
    success_url=reverse_lazy('home')


# def details(request,i):
#     k=Movie.objects.get(id=i)
#     context={'key':k}
#     return render(request,'details.html',context)


class Moviedetail(DetailView):
    model = Movie
    template_name = 'details.html'
    context_object_name = 'key'


# def delete(request,i):
#     p=Movie.objects.get(id=i)
#     p.delete()
#     return redirect('home')

class Moviedelete(DeleteView):
    template_name = 'delete.html'
    model = Movie
    success_url=reverse_lazy('home')


# def edit(request,i):
#     m=Movie.objects.get(id=i)
#     if(request.method=="POST"):
#         m.title=request.POST['t']
#         m.description=request.POST['d']
#         m.language=request.POST['l']
#         m.year=request.POST['y']
#         if(request.FILES.get('i')==None):
#             m.save()
#         else:
#             m.image=request.FILES.get('i')
#         m.save()
#         return redirect('home')
#     context={'k':m}
#     return render(request,'update.html',context)


class Movieupdate(UpdateView):
    template_name = 'edit.html'
    fields=['title','description','year','language','image']
    model=Movie
    success_url=reverse_lazy('home')


