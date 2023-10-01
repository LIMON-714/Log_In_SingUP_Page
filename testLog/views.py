from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import os
from django.contrib.auth import update_session_auth_hash


def homePage(request):
    return render(request, 'home.html')

def singupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:
            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'singup.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('password')
        user=authenticate(request,username=username,password=pass1)
        if user:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def Forget_password_Page(request):
    if request.method == 'POST':
         username=request.POST.get('username')
         email=request.POST.get('email')
         pass1=request.POST.get('password')
         pass2=request.POST.get('password2')
         if User is not None:
             user = User.objects.get(username=username)
             if user == user:
                if user.email == email:
                    if pass1==pass2:
                        user.set_password(pass1)
                        user.save()
                        update_session_auth_hash(request, user)
                        return redirect('login')
                    else:
                        return HttpResponse("Password are not same ....")
                
                else:
                    return HttpResponse("The Email is  not same ....")
         else:
             return HttpResponse("user is not correct....")
    return render(request,'forget.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')

