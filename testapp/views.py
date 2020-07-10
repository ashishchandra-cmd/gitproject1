from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from testapp.models import Register_table
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login ,logout, authenticate
# Create your views here.
def home_views(request):
    return render(request ,'home.html')
def admins_views(request):
    return render(request ,'admins.html')
def strocker_views(request):
    return render( request,'strocker.html')
def dispatcher_views(request):
    return render( request,'dispatcher.html')
def customer_views(request):
    return render( request,'customer.html')    

def login_view(request):
    return render(request,'logins.html') 

def register_views(request):
    if request.method=='POST':
        fname=request.POST['first']
        lname=request.POST['last']
        un=request.POST['uname']
        pwd=request.POST['password']
        em=request.POST['email']
        con=request.POST['contact']
        tp=request.POST['uType']

        usr=User.objects.create_user(un,em,pwd)
        usr.first_name=fname
        usr.last_name=lname
        if tp=='stro':
            usr.is_staff=True
        elif tp=='disp':
            usr.is_staff=True  
        elif tp=='cust' :
            usr.is_active=True    
        usr.save()
        reg=Register_table(user=usr, contect_number=con)
        reg.save()
        return HttpResponse('registation sesscefulyy')
    return render(request,'register.html')  

def user_login_view(request):
    if request.method=='POST':
        un=request.POST['username']
        pwd=request.POST['password']
        user=authenticate(username=un,password=pwd) 
        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect('/admins')
            elif user.is_staff:
                return HttpResponseRedirect('/strocker')
            elif user.is_staff:
                return HttpResponseRedirect('/dispatcher')
            elif user.is_active :
                return HttpResponseRedirect('/customer')      
        else:
            return render(request,'home.html',{'msg':'invalid user'})    
    return render 

def logout_view(request):
    logout(request)
    return redirect('/')  


def customerRegister(request):
    return render(request,'customerRegister.html')      
