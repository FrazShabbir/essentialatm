from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import useracc
import requests 
import datetime

# Create your views here.
def index(request):
    # products= addproduct.objects.order_by('-p_date_update').all()
    # return render(request,'index.html',{'products':products})
    return render(request,'index.html')


def signup(request):
    if request.method == 'POST':

         first_name = request.POST['first_name']
         last_name = request.POST['last_name']
         email= request.POST['email']
         username = request.POST['username']
         user_pass  = request.POST['pass1']
         pass2 = request.POST['pass2']
         user_balane = 0
         if user_pass == pass2:
             if User.objects.filter(username=username).exists():
                 messages.info(request,'Username Taken')
                 return redirect('signup')
             elif User.objects.filter(email=email).exists():
                 messages.info(request,'Email Taken')
                 return redirect('signup')
             else:
                 user1= User.objects.create_user(username=username, password=user_pass, email=email, first_name=first_name, last_name=last_name)
                 user1.save()
                 user = useracc(username=username, user_pass=user_pass, email=email, first_name=first_name, last_name=last_name,balance=user_balane)
                 user.save()
                 return redirect('/')
  
             return redirect('/')
         else:
             messages.info(request,'Password Not matching')
             return redirect('signup')

    else:
         return render(request,"sign-up.html")






def signin(request):
    if request.method=='POST':
        username=request.POST['email']
        password=request.POST['password']
        
        user1 = auth.authenticate(username=username,password=password)

        if user1 is not None:
            auth.login(request,user1)
            getuser=request.user
            blogs= blogsSection.objects.filter(author=getuser).order_by('-B_date')
            return render(request,"index.html" )
        else:
            messages.info(request,"Incorrect Username or Password")
            return render(request,"sign-in.html")


    else:
        return render(request,"sign-in.html")

def logout(request):
    auth.logout(request)
    return redirect('/')