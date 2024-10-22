from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from adminside.models import Manager
from .models import Waiter,Chef,Tables
from adminside.models import Manager
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.decorators import login_required

# Create your views here.
def managerlogin(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')

        manager = authenticate(request,username=username, password=password)
       
        if manager is not None:
            
            login(request,manager,backend='manager.backends.ManagerBackend')
            return redirect('managerdashboard')

    return render(request,'manager/login.html')

# @login_required(login_url="/manager/managerlogin/") 
def managerlogout(request):
    logout(request)
    return redirect('managerlogin')

# @login_required(login_url="/manager/managerlogin/") 
def managerdashboard(request):
    if isinstance(request.user, Manager):
        manager = request.user
        print(manager)
    context={
        'managerdashboard':True
    }
    return render(request,'manager/index.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def addwaiter(request):
    if request.method=='POST':
        waitername = request.POST.get('waitername')
        waiteremail=request.POST.get('waiteremail')

        existswaiter = Waiter.objects.filter(waiteremail=waiteremail).exists()
        if existswaiter:
            messages.error(request,'Waiter is already there! first you have to delete that Waiter',extra_tags='existswaiter')
            return  redirect('addwaiter')
        else:
            Waiter.objects.create(waitername=waitername,waiteremail=waiteremail,waiterpassword=make_password('Waiter@123'))
            messages.success(request,'Waiter is Added...',extra_tags='waiteradd')
            return redirect('addwaiter')
    context={
        'addwaiter':True
        }
    return render(request,'manager/addwaiter.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def listofwaiter(request):
    waiters = Waiter.objects.all()
    context={
        'listofwaiter':True,
        'waiters':waiters
    }
    return render(request,'manager/listofwaiter.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def addchef(request):
    if request.method=='POST':
        chefname = request.POST.get('chefname')
        chefemail=request.POST.get('chefemail')

        existschef = Chef.objects.filter(chefemail=chefemail).exists()
        if existschef:
            messages.error(request,'chef is already there! first you have to delete that chef',extra_tags='existschef')
            return  redirect('addchef')
        else:
            Chef.objects.create(chefname=chefname,chefemail=chefemail,chefpassword=make_password('Chef@123'))
            messages.success(request,'chef is Added...',extra_tags='chefadd')
            return redirect('addchef')
    context={
        'addchef':True
    }
    return render(request,'manager/addchef.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def listofchef(request):
    chefs = Chef.objects.all()
    context={
        'listofchef':True,
        'chefs':chefs
    }
    return render(request,'manager/listofchef.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def changepassword(request):
    if request.method=='POST':
        oldpassword = request.POST.get('oldpassword')
        newpassword = request.POST.get('newpassword')
        id = request.user.id
        manager = Manager.objects.get(pk=id)
        newhashpassword = make_password(newpassword)
        
        if check_password(oldpassword,manager.managerpassword):
            data = {
                'managerpassword':newhashpassword
            }
            Manager.objects.update_or_create(pk=id,defaults=data)
            messages.success(request,'Password is Change',extra_tags='passwordchangemanager')
        else:
            messages.error(request,'old password is not right plz chek...',extra_tags='notchangepasswordmanager')
    context={
        'changepassword':True
    }
    return render(request,'manager/changepassword.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def addtable(request):
    if request.method == 'POST':
        tableNo = request.POST.get('tableNo')
        tableSize = request.POST.get('tableSize')

        tableExists = Tables.objects.filter(tableNo=tableNo).exists()
        if tableExists:
            messages.error(request,'This Table No is already exists',extra_tags='existstable')
            return redirect('addtable')

        Tables.objects.create(tableNo=tableNo,tableSize=tableSize)
        messages.success(request,'Table is Add..',extra_tags='tableadd')
        return redirect('addtable')

    context={
        'addtable':True
    }
    return render(request,'manager/addtable.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def listoftable(request):
    tables = Tables.objects.all()
    context = {
        'listoftable':True,
        'tables':tables
    }
    return render(request,'manager/listoftable.html',context)

# @login_required(login_url="/manager/managerlogin/") 
def deletechef(request,id):
    chef = Chef.objects.get(pk=id)
    chef.delete()
    return redirect('listofchef')

# @login_required(login_url="/manager/managerlogin/") 
def deletewaiter(request,id):
    waiter = Waiter.objects.get(pk=id)
    waiter.delete()
    return redirect('listofwaiter')

# @login_required(login_url="/manager/managerlogin/") 
def deletetable(request,id):
    table = Tables.objects.get(pk=id)
    table.delete()
    return redirect('listoftable')