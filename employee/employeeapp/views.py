from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,'home.html')

from employeeapp.models import Employee
def addemployee(request):
    if(request.method=="POST"):
        empid=request.POST['id']
        name=request.POST['n']
        age=request.POST['a']
        salary=request.POST['s']
        location=request.POST['l']
        designation=request.POST['d']
        image=request.FILES.get('img')
        k=Employee.objects.create(empid=empid,name=name,age=age,salary=salary,location=location,designation=designation,image=image)
        k.save()
        return redirect('home')
    return render(request,'addemployee.html')

def viewemployeelist(request):
    k=Employee.objects.all()
    context={'key':k}
    return render(request,'viewemployeelist.html',context)

def delete(request,i):
    k=Employee.objects.get(id=i)
    k.delete()
    return redirect('home')

def edit(request,i):
    p=Employee.objects.get(id=i)
    if(request.method=="POST"):
        p.empid=request.POST['id']
        p.name = request.POST['n']
        p.age = request.POST['a']
        p.salary = request.POST['s']
        p.location = request.POST['l']
        p.designation=request.POST['d']
        if (request.FILES.get('img') == None):
            p.save()
        else:
            p.image=request.FILES.get('img')

        p.save()
        return redirect('home')

    context={'key':p}
    return render(request,'edit.html',context)


