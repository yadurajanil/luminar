from django.db.models import Q
from django.shortcuts import render, redirect
from books.models import Books
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request,"home.html")

@login_required
def add(request):
    if request.method=="POST":
        tit=request.POST['t']
        aut=request.POST['a']
        pri=request.POST['p']
        pag=request.POST['pg']
        lan=request.POST['l']
        img=request.FILES['i']
        pdf=request.FILES['f']
        b=Books.objects.create(title=tit,author=aut,price=pri,pages=pag,language=lan,image=img,pdf=pdf)
        b.save()
        return redirect('books:view')

    return render(request,"add.html")

@login_required
def view(request):
    b=Books.objects.all()
    context={'book':b}
    return render(request,"view.html",context)

@login_required
def factorial(request):
    if request.method=="POST":
        num=int(request.POST['n'])
        f=1
        for i in range(1,num+1):
            f=f*i
        return render(request,'factorial.html',{'fact':f})


    return render(request,'factorial.html')

@login_required
def detailview(request,i):
    b=Books.objects.get(id=i)
    context={'book':b}
    return render(request,'detailview.html',context)

@login_required
def deletebook(request,i):
    b=Books.objects.get(id=i)
    b.delete()
    return redirect('books:view')

@login_required
def edit(request,i):
    b=Books.objects.get(id=i)
    if request.method=="POST":
        b.title=request.POST['t']
        b.author=request.POST['a']
        b.price=request.POST['p']
        b.pages=request.POST['pg']
        b.language=request.POST['l']
        if request.FILES.get('i')==None:
            b.save()
        else:
            b.image=request.FILES.get('i')
        if request.FILES.get('f')==None:
            b.save()
        else:
            b.pdf=request.FILES.get('f')
            b.save()
        return redirect('books:view')
    context={'book':b}
    return render(request,'edit.html',context)

def search(request):
    if request.method=="POST":
        query=request.POST['q']
        b=Books.objects.filter(Q(title__icontains=query)| Q(author__icontains=query))
        context={'book':b}
    return render(request,'search.html',context)