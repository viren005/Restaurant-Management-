from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from waiter.models import Order
# Create your views here.

def cheflogin(request):
    if request.method == 'POST':
        username = request.POST.get('chefemail')
        password = request.POST.get('password')

        chef = authenticate(request,username=username, password=password)
        print(chef)
         
        if chef is not None:
            # Waiter.objects.update_or_create(is_authenticated=True)
            login(request,chef,backend='chef.backends.ChefBackend')
            print('i am in if condition')
            print(request.user.id)
            session_items = request.session.items()
            print(session_items)
            return redirect('neworder')
        else:
            messages.error(request,'Username or Password Unvalid',extra_tags='chefloginerror')
            return redirect('cheflogin')
    return render(request,'chef/login.html')

def neworder(request):
    id = request.user.id
    session_items = request.session.items()
    print(session_items)
    neworders = Order.objects.filter(status="pending")
    context = {
        'neworder':True,
        'neworders':neworders
    }
    return render(request,'chef/index.html',context)

def complete(request,id):
    completeorders =  Order.objects.filter(id=id).update(status='complete')
    return redirect('neworder')

def completeorder(request):
    completorders = Order.objects.filter(status="complete")
    context={
        'completorders':completorders
    }
    return render(request,'chef/completeorder.html',context)


def changepassword(request):
    context = {
        'changepasswordchef':True
    }
    return render(request,'chef/changepassword.html',context)

def cheflogout(request):
    logout(request)
    return redirect('cheflogin')