import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Udetails,Booktable,Cart_itmes,Cart
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from adminside.models import Product,Banner,Category
from django.db.models import Sum


#Client-side views

def register(request):
    if request.method =='POST':

        name = request.POST.get('name')
        uname = request.POST.get('uname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        password = request.POST.get('password')

        existsuser = User.objects.filter(username=uname).exists()
        existsmail = User.objects.filter(email=email).exists()
       
        if existsuser:
            uerror = "Username is already taken"
            context = {
                'name':name,
                'uname':uname,
                'email':email,
                'phone':phone,
                'city':city,
                'uerror':uerror
            }
            return render(request,'client/register.html',context)
        
        if existsmail:
            error = "Email is already Register"
            context = {
                'name':name,
                'uname':uname,
                'email':email,
                'phone':phone,
                'city':city,
                'error':error
            }
            return render(request,'client/register.html',context)
        
        user = User.objects.create_user(first_name=name,username=uname,email=email,password=password)
        
        uid = user.id
        Udetails.objects.create(uid_id=uid,phone=phone,city=city)
        return redirect('login')
    else:
        return render(request,'client/register.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password) 
        if user is not None:
            if user.is_superuser:
                msg='Unvalid Username or Password!!'
                context = {
                    'msg':msg
                }
                if msg:
                    return render(request,'client/login.html',context)
            else:
                auth.login(request, user)
                return redirect('home')
        else:
            msg='Unvalid Username or Password!!'
            context = {
                'msg':msg
            }
            if msg:
                return render(request,'client/login.html',context)
    
        
    return render(request,'client/login.html')

def home(request):
    products = list(Product.objects.all())
    random.shuffle(products)
    items = products[:6]
    banners = Banner.objects.all()
    categorys = Category.objects.all()
    context={
        'home':True,
        'items':items,
        'banners':banners,
        'categorys':categorys
    }
    return render(request,'client/index.html',context)

# @login_required(login_url="/restaurantapp/login/")
def menu(request):
    items = Product.objects.all()
    categorys = Category.objects.all()
    context={
        'menu':True,
        'items':items,
        'categorys':categorys
    }
    return render(request,'client/menu.html',context)

# @login_required(login_url="/restaurantapp/login/")
def about(request):
    context={
        'about':True
    }
    return render(request,'client/about.html',context)

@login_required(login_url="/restaurantapp/login/")
def booktable(request):
    context={
        'book':True
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        numberofper = request.POST.get('numberofper')
        date = request.POST.get('date')

        uid = request.user.id
        
        Booktable.objects.create(uid_id=uid,name=name,phone=phone,email=email,numberofper=numberofper,date=date)
        return redirect('home')
    return render(request,'client/book.html',context)

@login_required(login_url="/restaurantapp/login/")  
def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="/restaurantapp/login/")
def cart(request):
    uId = request.user.id
    cart = Cart.objects.filter(user = uId)
    # print(cart)
    if cart:
       cartItems = Cart_itmes.objects.filter(cartid = cart[0].id)
       totalPrice  = cartItems.aggregate(total = Sum('itemTotal'))
       totalItems  = cartItems.aggregate(totalItems = Sum('quantity'))
       totalPrice = totalPrice['total']
       totalItems = totalItems['totalItems']
    #    for item in cartItems:
    #     totalItems += item.quantity
    #     totalPrice += item.itemTotal

       
    
       context={
           'cartItems':cartItems,
           'totalItems':totalItems,
           'totalPrice':totalPrice,
           
       }
    return render(request,'client/cart.html',context)

@login_required(login_url="/restaurantapp/login/")
def addtocart(request,id,action):
    # product = Product.objects.get(pk=id)
    product = id
    uId =  request.user.id
    user = Cart.objects.filter(user = uId).exists()
    if user:
        cart = Cart.objects.values('id').get(user = uId)
        checkCartitem = Cart_itmes.objects.filter(cartid = cart['id'] , product= product)
 
        if checkCartitem:
            cartItem = Cart_itmes.objects.get(cartid = cart['id'], product = product)
            if action =='increment':
                cartItem.quantity += 1
                cartItem.save() 
                return redirect('cart')
            elif action=='decrement':
                if cartItem.quantity > 1:
                    cartItem.quantity -= 1
                    cartItem.save() 
                    return redirect('cart')
                else:
                    cartItem.delete()
                    return redirect('cart')
        else:
            cart = Cart.objects.values('id').get(user = uId)
            Cart_itmes.objects.create(cartid_id=cart['id'],product_id=product)
            return redirect('cart')    
    else:
        Cart.objects.create(user_id=uId)
        cart = Cart.objects.values('id').get(user = uId)
        Cart_itmes.objects.create(cartid_id=cart['id'],product_id=product)
        return redirect('cart')

@login_required(login_url="/restaurantapp/login/")    
def deletecartItem(request,id):
    cartItem = Cart_itmes.objects.get(pk=id)
    cartItem.delete()
    return redirect('cart')

@login_required(login_url="/restaurantapp/login/")  
def categoryproduct(request,id):
    items = Product.objects.filter(pcid_id=id)
    categorys = Category.objects.all()
    context = {
        'menu':True,
        'items':items,
        'categorys':categorys,
        'activeCategory':id
    }
    return render(request,'client/menu.html',context)


@login_required(login_url="/restaurantapp/login/")  
def profile(request):
    return render(request,'client/profile.html')


