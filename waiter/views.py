from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from manager.models import Tables, Waiter
from adminside.models import Product,Category
from .models import Waitercart,Order,TempOrder
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def waiterlogin(request):
    if request.method == 'POST':
        username = request.POST.get('waiteremail')
        password = request.POST.get('password')

        waiter = authenticate(request,username=username, password=password)
        print(waiter)
        
        if waiter is not None:
            # Waiter.objects.update_or_create(is_authenticated=True)
            login(request,waiter,backend='waiter.backends.WaiterBackend')
            print('i am in if condition')
            print(request.user.id)
            session_items = request.session.items()
            print(session_items)
            return redirect('waiterdashboard')
        else:
            messages.error(request,'Username or Password Unvalid',extra_tags='waiterloginerror')
            return redirect('waiterlogin')
    return render(request,'waiter/login.html')

# @login_required(login_url="/waiter/waiterlogin/")
def waiterlogout(request):
    logout(request)
    return redirect('waiterlogin')

# @login_required(login_url="/waiter/waiterlogin/")
def waiterdashboard(request):
    sid = request.session.get('_auth_user_id')
    print("waiterid",sid)
    id = request.user.id
    print(request.session.items)
    print("waiterdashboard:",id)
    if str(sid) == str(id):
        print('User is a waiter, granting access to dashboard.')
        tables = Tables.objects.all()
        context = {
            'waiterdashboard': True,
            'tables': tables
        }
        return render(request, 'waiter/index.html', context)
    else:
        # If the session user ID and waiter ID do not match, redirect to login or unauthorized access page
        print('User is not authorized to view this page.')
        return redirect('login')  # or redirect to an unauthorized access page
       
# @login_required(login_url="/waiter/waiterlogin/")
def changepasswordwaiter(request):
    context={
        'changepasswordwaiter':True
    }
    return render(request,'waiter/changepassword.html',context)

# @login_required(login_url="/waiter/waiterlogin/")
def waitermenu(request,tableno,category):
    waiterid = request.user.id
    category = category
    if category == 'allcategory':
        items = Product.objects.all()
        categorys = Category.objects.all()
        waitercart = Waitercart.objects.filter(wid=waiterid,tableno=tableno)
        temptable = TempOrder.objects.filter(tableno_id=tableno)
        if waitercart is not None:
            context={
                'items':items,
                'categorys':categorys,
                'activeCategory':'',
                'tableNo':tableno,
                'waitercart':waitercart,
                'temptable':temptable
            }
            return render(request,'waiter/waitermenu.html',context)
        else:
            context={
                'items':items,
                'categorys':categorys,
                'activeCategory':'',
                'tableNo':tableno,
                
            }
            return render(request,'waiter/waitermenu.html',context)
        
    else:
        items = Product.objects.filter(pcid_id=category)
        categorys = Category.objects.all()
        waitercart = Waitercart.objects.filter(wid=waiterid,tableno=tableno)
        temptable = TempOrder.objects.filter(tableno_id=tableno)
        if waitercart is not None:
            context={
                'items':items,
                'categorys':categorys,
                'activeCategory':int(category),
                'tableNo':tableno,
                'waitercart':waitercart,
                'temptable':temptable
            }
            return render(request,'waiter/waitermenu.html',context)
        else:
            context={
                'items':items,
                'categorys':categorys,
                'activeCategory':int(category),
                'tableNo':tableno,
            }
            return render(request,'waiter/waitermenu.html',context)

# @login_required(login_url="/waiter/waiterlogin/")
def waitercart(request,tableno,productid,action):
    waiterid = request.user.id
    print("waiterid:",waiterid)
    try:
        waitercart = Waitercart.objects.get(wid=waiterid,tableno=tableno,pid=productid)
        if action=='increment':
            waitercart.pquantity +=1
            waitercart.save()
        elif action =='decrement':
            if waitercart.pquantity>1:
                waitercart.pquantity -=1
                waitercart.save()
            else:
                waitercart.delete()
        return redirect('waitermenu',waitercart.tableno.id,waitercart.pid.pcid.id)
    except Waitercart.DoesNotExist:
        waitercart = Waitercart.objects.create(wid_id=waiterid,tableno_id=tableno,pid_id=productid)
        if action=='increment':
            waitercart.pquantity +=1
            waitercart.save()
        elif action =='decrement':
            if waitercart.pquantity>1:
                waitercart.pquantity -=1
                waitercart.save()
            else:
                waitercart.delete()
        return redirect('waitermenu',waitercart.tableno.id,waitercart.pid.pcid.id)

# @login_required(login_url="/waiter/waiterlogin/")
def proceed(request,tableno):
    waiterid = request.user.id
    print(request.session.items())
    cartitems = Waitercart.objects.filter(wid=waiterid,tableno=tableno)
   
    if cartitems.exists():
        for item in cartitems:
            Order.objects.create(wid=item.wid,tableno=item.tableno,productname=item.pid.pname,pquantity=item.pquantity)
            TempOrder.objects.create(wid=item.wid,tableno=item.tableno,productname=item.pid.pname,pquantity=item.pquantity)
            Tables.objects.filter(id=tableno).update(isActive='open')
            Waitercart.objects.filter(tableno_id=tableno).delete()
        messages.success(request,f'Order of Table No {tableno} Passed To chef...',extra_tags='orderpass')
        return redirect('waiterdashboard')

    return redirect('waitermenu')



def complateorder(request,tableno):
    
    Tables.objects.filter(id=tableno).update(isActive='close')
    return redirect('waiterdashboard')
