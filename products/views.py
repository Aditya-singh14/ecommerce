from django.shortcuts import render,redirect
from products.models import *

from django.contrib.auth.models import User                      #Django provides built in table to store authentication data
from django.contrib import messages                              #Used to display that user has been registered
from django.contrib.auth import authenticate, login, logout




#Create your views here.

def index(request):
    category =Category.objects.all()
    product =Product.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        product=Product.objects.filter(sub_category=categoryID).order_by('-id')
    else:
        product=Product.objects.all()
    # sub_category=Sub_Category.objects.all()
    context={
        'category':category,
        'product':product,
        # 'sub_category':sub_category
    }
    return render(request,'index.html',context)


# def register(request):
#     if request.method=='POST':
#         email=request.POST.get('email')
#         password=request.POST.get('password')
#         username=request.POST.get('name')
#         if User.objects.filter(email=email).exists():                             # Condition for same email id if already exists
#             messages.warning(request,'Email already exists')
#             return redirect('login')
#         else:
#             user =User(email=email,password=password,username=username)
#             user.set_password(password)                                             #since raw passwords are not saved therefore needs to set in this method
#             user.save()
#             messages.success(request,'User has been registered successfully')      #Dispalys message that user has been registerd 
#             return redirect('login')
#         # print(email,password,username)
#     return render (request,'login.html')

# def login_user(request):
#     if request.method=='POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect ('/')
#         else:
#             messages.warning(request,'Invalid credentials')
#             return redirect('login')
#     return render (request,'login.html')

def login_user(request):
    if request.method=='POST':
        
        if request.POST.get('submit')=='sign_up':
            
            username=request.POST.get('name')
            email=request.POST.get('email')
            password=request.POST.get('password')
            
            if User.objects.filter(email=email).exists():                             # Condition for same email id if already exists
                messages.warning(request,'Email already exists')
            else:
                user =User(email=email,password=password,username=username)
                user.set_password(password)                                             #since raw passwords are not saved therefore needs to set in this method
                user.save()
                messages.success(request,'User has been registered successfully')      #Dispalys message that user has been registerd 
            return redirect('login')

        elif request.POST.get('loginsubmit')=='sign_in':
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect ('/')
            else:
                messages.warning(request,'Invalid credentials')
        # print(email,password,username)
    return render (request,'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')

