from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import useracc
import datetime
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


# Create your views here.
def index(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    return render(request,"index.html",{'details':details})


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
                 return render(request,"sign-in.html")
  
             return redirect('signup')
         else:
             messages.info(request,'Password Not matching')
             return redirect('signup')

    else:
         return render(request,"sign-up.html")






def signin(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user1 = auth.authenticate(username=username,password=password)

        if user1 is not None:
            auth.login(request,user1)
            getuser=request.user
            details= useracc.objects.get(username=getuser)
            return render(request,"index.html",{'details':details})
        else:
            messages.info(request,"Incorrect Username or Password")
            return render(request,"sign-in.html")


    else:
        return render(request,"sign-in.html")

def logout(request):
    auth.logout(request)
    return redirect('/')


def amount(request):
    if request.method=='POST':
        amount=request.POST['enteredamount']
        getuser=request.user
        details= useracc.objects.get(username=getuser)
        prebal = details.balance
        newbal=details.balance-int(amount)
        withdraw=int(amount)
        details.balance=newbal
        details.save()
        details= useracc.objects.get(username=getuser)
        return render(request,"checkout.html",{'details':details, 'prebal':prebal,'withdraw':withdraw})

    else:
        getuser=request.user
        details= useracc.objects.get(username=getuser)
        return render(request,"amount.html",{'details':details})


def deposit(request):
    if request.method=='POST':
        amount=request.POST['enteredamount']
        getuser=request.user
        details= useracc.objects.get(username=getuser)
        prebal = details.balance
        newbal=prebal+int(amount)
        submitted=int(amount)
        details.balance=newbal
        details.save()
        details= useracc.objects.get(username=getuser)
        return render(request,"thankyou.html",{'newbal':newbal, 'prebal':prebal,'submitted':submitted})

    else:
        return render(request,"deposit.html")




def balanceinq(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    return render(request,"balanceinq.html",{'details':details})


def gethelp(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    return render(request,"gethelp.html",{'details':details})

def quickamount(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    return render(request,"quickbalance.html",{'details':details})

def checkout(request):
    return render(request,"checkout.html")

def baltenk(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    prebal = details.balance
    withdraw=10000
    newbal=details.balance-10000
    details.balance=newbal
    details.save()
    details= useracc.objects.get(username=getuser)
    return render(request,"checkout.html",{'details':details, 'prebal':prebal,'withdraw':withdraw})


def balfivek(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    prebal = details.balance
    newbal=details.balance-5000
    withdraw=5000
    details.balance=newbal
    details.save()
    details= useracc.objects.get(username=getuser)
    return render(request,"checkout.html",{'details':details, 'prebal':prebal,'withdraw':withdraw})

def balfifk(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    prebal = details.balance
    newbal=details.balance-15000
    withdraw=15000
    details.balance=newbal
    details.save()
    details= useracc.objects.get(username=getuser)
    return render(request,"checkout.html",{'details':details, 'prebal':prebal,'withdraw':withdraw})

def baltwk(request):
    getuser=request.user
    details= useracc.objects.get(username=getuser)
    prebal = details.balance
    newbal=details.balance-20000
    withdraw=20000
    details.balance=newbal
    details.save()
    details= useracc.objects.get(username=getuser)
    return render(request,"checkout.html",{'details':details, 'prebal':prebal,'withdraw':withdraw})












def printpdf(request):
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.drawString(0, 10, "Hello world.")
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='essentialbank.pdf')