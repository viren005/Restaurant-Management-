from django.shortcuts import redirect, render,HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings 
import os
from django.contrib.auth.models import User 
from django.contrib import auth,messages
from .models import Category,Product,Banner,Manager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
# Create your views here.

#Admin-side views

def login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')

        if User.objects.filter(username=username, is_superuser=True).exists():
            user = auth.authenticate(username=username, password=password) 
            if user is not None:
                auth.login(request, user)
                return redirect('admin')
        else:
            msg='Unvalid Username or Password!!'
            context = {
                    'msg':msg
                }
            if msg:
                return render(request,'admin/login.html',context)
            return render(request,'admin/login.html')
    return render(request,'admin/login.html')

@login_required(login_url="/adminside/loginadmin/")  
def logout(request):
    auth.logout(request)
    return redirect('loginadmin')

@login_required(login_url="/adminside/loginadmin/") 
def storeproduct(request):
    name = request.POST.get('pname')
    description = request.POST.get('pdes')
    price = request.POST.get('pprice')
    pcategory = request.POST.get('category')
    image = request.FILES['pimage'] # file data
    location = os.path.join(settings.MEDIA_ROOT,'food')
    obj  = FileSystemStorage(location=location)

    extname = Product.objects.filter(pname=name).exists()
    if extname:
        messages.error(request,'this items name is already there!! so try new name',extra_tags='alreadyexists')
        return redirect('addproduct')
    


    ext = ['png','jpeg','jpg']
    iname = image.name
    e = iname.split('.')
    e = e[-1]

    if e in ext:
     obj.save(image.name,image)
     url = f'../../../media/food/{image.name}'

     Product.objects.create(pname=name,description=description,price=price,pcid_id=pcategory,image=url)
     messages.success(request,'Product added successfully',extra_tags='foodadded')
     
     return redirect('addproduct')
    else:
       print('it\'s not working')
       return HttpResponse('file is not saved')

@login_required(login_url="/adminside/loginadmin/") 
def admin(request):
    context={
        'admin':True
    }
    return render(request,'admin/index.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def addproduct(request):  
    categorys = Category.objects.all()
    context = {
        'categorys':categorys,
        'addproduct':True
    }  
    return render(request,'admin/addproduct.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def addcategory(request): 
    context = {
        'addcategory':True
    }   
    if request.method =='POST':
        categoryname = request.POST.get('categoryname')
        
        existcategory = Category.objects.filter(categoryname=categoryname).exists()
        if existcategory:
            msg = 'This category is already exists'
            context = {
                'categorys':categoryname,
                'msg':msg
            }
            return render(request,'admin/addcategory.html',context)
        else:
            Category.objects.create(categoryname=categoryname)
            return render(request,'admin/addcategory.html')
            
    return render(request,'admin/addcategory.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def listofproduct(request):
    product = Product.objects.select_related('pcid').all()
    context = {
        'product':product,
        'listofproduct':True
    }
    return render(request,'admin/listofproduct.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def deleteproduct(request,id):
    deletepro =  Product.objects.get(pk=id)
    deletepro.delete()
    return redirect('listofproduct')

@login_required(login_url="/adminside/loginadmin/") 
def updateproduct(request,id):
    if request.method == "POST":
        name = request.POST.get('pname')
        description = request.POST.get('pdes')
        price = request.POST.get('pprice')
        pcategory = request.POST.get('category')
        if 'pimage' in request.FILES:
            print('img1')
            image = request.FILES['pimage'] # file data
            location = os.path.join(settings.MEDIA_ROOT,'food')
            obj  = FileSystemStorage(location=location)
            ext = ['png','jpeg','jpg']
            iname = image.name
            e = iname.split('.')
            e = e[-1]
            if e in ext:
                obj.save(image.name,image)
                url = f'../../../media/food/{image.name}'
                extname = Product.objects.filter(pname=name).exists()
                if extname:
                    data = {
                        'description':description,
                        'price':price,
                        'pcid_id':pcategory,
                        'image':url
                    }
                    Product.objects.update_or_create(pk=id,defaults=data)
                    return redirect('updateproduct',id)
                
        extname = Product.objects.filter(pname=name).exists()
        if extname:
            data = {
                'description':description,
                'price':price,
                'pcid_id':pcategory
            }
            Product.objects.update_or_create(pk=id,defaults=data)
            return redirect('updateproduct',id)
        else:
            data = {
                        'pname':name,
                        'description':description,
                        'price':price,
                        'pcid_id':pcategory,
                    }
            Product.objects.update_or_create(pk=id,defaults=data)
            return redirect('updateproduct',id)
    else:
        data = Product.objects.select_related('pcid').get(pk=id)
        categorys = Category.objects.all()
        context = {
            'data':data,
            'categorys':categorys
        }
        return render(request,'admin/updateproduct.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def deletecategory(request,id):
    deletecategory =  Category.objects.get(pk=id)
    deletecategory.delete()
    return redirect('listofcategory')

@login_required(login_url="/adminside/loginadmin/") 
def listofcategory(request):
    categorys = Category.objects.all()
    context = {
        'categorys':categorys,
        'listofcategory':True
    }
    return render(request,'admin/listofcategory.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def addbanner(request):
    context={
        'addbanner':True
    }
    if request.method == 'POST':
        bannername = request.POST.get('bannername')
        bannerdescription = request.POST.get('bannerdescription')
        # bannerimage = request.FILES['bannerimage']
        # location = os.path.join(settings.MEDIA_ROOT,'banner')
        # obj = FileSystemStorage(location=location)

        # ext = ['png','jpeg','jpg']
        # image = bannerimage.name
        # extentionchek = image.split('.')
        # extentionchek = extentionchek[-1]
        
        # if extentionchek in ext:
        #     obj.save(bannerimage.name,bannerimage)
        #     url = f'../../../media/banner/{bannerimage.name}'

        Banner.objects.create(bannername=bannername,bannerdescription=bannerdescription)
        return redirect('addbanner')    
    return render(request,'admin/addbanner.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def addmanager(request):
    if request.method=='POST':
        managername = request.POST.get('managername')
        manageremail=request.POST.get('manageremail')

        existsmanager = Manager.objects.all()
        if existsmanager:
            messages.error(request,'Manager is already there! first you have to delete that manager',extra_tags='existsmanager')
            return  redirect('addmanager')
        else:
            Manager.objects.create(managername=managername,manageremail=manageremail,managerpassword=make_password('Manager@123'))
            messages.success(request,'Manager is Added...',extra_tags='manageradd')
            return redirect('addmanager')
    context={
        'addmanager':True
    }
    return render(request,'admin/addmanager.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def listofmanager(request):
    managers = Manager.objects.all()
    context={
        'listofmanager':True,
        'managers':managers
    }
    return render(request,'admin/listofManager.html',context)

@login_required(login_url="/adminside/loginadmin/") 
def deletemanager(request,id):
    manager = Manager.objects.get(pk=id)
    manager.delete()
    return redirect('listofmanager')
