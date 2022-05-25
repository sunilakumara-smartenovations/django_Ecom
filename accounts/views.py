from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import login
from .models import * 
from .max import MessaHandler
import random

# Create your views here.


def login_view(request):
    if request.method == 'POST':
        phone_no = request.POST.get('phone_no')
        profile= Profile.objects.filter(phone_no = phone_no)
        if not profile.exists():
            return redirect('/register')

        profile[0].otp = random.randint(1000,9999)
        profile[0].save()
        message_handler = MessaHandler(phone_no, profile[0].otp).send_otp_on_phone()
        return redirect (f'/otp/{profile[0].uid}')
    return render(request, 'login.html')

def register_view(request):
     if request.method == 'POST':
         username = request.POST.get('username')
         phone_no = request.POST.get('phone_no')
         user = User.objects.create(username = username)
         profile = profile.objects.create(user = user , phone_no = phone_no)

     return render(request, 'register.html')


def dashboard_view(request):
    return render(request,"dashboard.html")

def otp(request , uid): 
    if request.method == 'POST':
        otp = request.POST.get('otp')
        profile = Profile.objects.get(uid = uid)
        if otp == profile.otp:
            login(profile.user,request)
            return redirect('/dashboard')
        return redirect (f'/otp/{uid}')

    return render(request,"otp.html")



# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user= auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'invalid user or password')
#             return redirect('login')

#     else:
#         return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST' :
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         email = request.POST['email']
#         if password1 == password2:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username taken')
#                 return redirect('register')
#                 #print('username taken')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email taken')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
#                 user.save();
#                 messages.info(request,'User created')
#                 return redirect('login')
#         else:
#             messages.info(request,'password not matching')
#         return redirect('register')
#     else:
#         return render(request,'register.html')


# def logout(request):
#     auth.logout(request)
#     return redirect('/')