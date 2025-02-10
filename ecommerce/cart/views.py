import razorpay
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from shop.models import Product
from cart.models import Cart

from cart.models import Payment,Order_Details


@login_required
def add_to_cart(request,pk):
    p=Product.objects.get(id=pk)
    u=request.user
    try:
        c=Cart.objects.get(user=u,product=p)#if product is already present inside table for the current user
        c.quantity+=1  #it will increment the quantity inside the record
        p.stock-=1
        p.save()
        c.save()
    except: #if not present
        c=Cart.objects.create(product=p,user=u,quantity=1) #it will add a new record with quantity =1
        p.stock-=1
        p.save()
        c.save()
    return redirect('cart:cart_view')



@login_required
def cart_view(request):
    u=request.user
    c=Cart.objects.filter(user=u)
    total = 0
    for i in c:
        total += i.quantity * i.product.price
    context={'cart':c,'total':total}
    return render(request,'cart.html',context)



def cart_decrement(request,pk):
    p=Product.objects.get(id=pk)
    u = request.user
    try:
        c=Cart.objects.get(user=u,product=p)
        if(c.quantity>1):
            c.quantity= c.quantity -1
            c.save()
            p.stock +=1
            p.save()
        else:
            c.delete()
            p.stock =p.stock +1
            p.save()
    except:
        pass
    return redirect('cart:cart_view')



def cart_delete(request,pk):
    p=Product.objects.get(id=pk)
    u = request.user
    try:
        c = Cart.objects.get(user=u, product=p)
        c.delete()
        p.stock += c.quantity
        p.save()
    except:
        pass

def orderform(request):
    if(request.method=="POST"):
        a = request.POST['u']
        pn= request.POST['p']
        n = request.POST['pi']
        u = request.user
        c = Cart.objects.filter(user=u)
        total=0
        for i in c:
            total+=i.product.price*i.quantity
        print(total)
        total=int(total)
        client = razorpay.Client(auth=('rzp_test_gblkaFnbfR9Z0f','ClHAtZGAzwnmMJ3RwY6tIDFm'))
        response_payment = client.order.create(dict(amount=total*100, currency='INR'))
        print(response_payment)
        order_id = response_payment['id']
        status = response_payment['status']
        if (status == "created"):
            p = Payment.objects.create(name=u.username, amount=total, order_id=order_id)
            p.save()
            for i in c:
                o = Order_Details.objects.create(product=i.product, user=i.user, phone=pn, address=a, pin=n,
                                                 order_id=order_id, no_of_items=i.quantity)
                o.save()
            context={'payment':response_payment,'name':u.username}
            return render(request, 'payment.html',context)
    return render(request,'orderform.html')



@csrf_exempt
def payment_status(request,k):
    user=User.objects.get(username=k)
    login(request,user)
    response=request.POST
    print(response)
    param_dict={
        'razorpay_order_id':response['razorpay_order_id'],
        'razorpay_payment_id': response['razorpay_payment_id'],
        'razorpay_signature': response['razorpay_signature'],
         }
#
    client=razorpay.Client(auth=('rzp_test_gblkaFnbfR9Z0f','ClHAtZGAzwnmMJ3RwY6tIDFm'))
    try:
        status=client.utility.verify_payment_signature(param_dict)
        print(status)
        m = Payment.objects.get(order_id=response['razorpay_order_id'])
        m.paid = True
        m.razorpay_payment_id = response['razorpay_payment_id']
        m.save()
        o = Order_Details.objects.filter(order_id=response['razorpay_order_id'])
        for i in o:
            i.payment_status = "Completed"
            i.save()

        c=Cart.objects.filter(user=user)
        c.delete()
    except:
        pass
    return render(request,'paymentstatus.html')



def your_orders(request):
    u=request.user
    o=Order_Details.objects.filter(user=u,payment_status='completed')
    context={'orders':o}
    return render(request,'yourorders.html',context)










