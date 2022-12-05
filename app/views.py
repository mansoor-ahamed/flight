from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Contact,Post,Flight
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage




# Create your views here.
def front(request):
    return render(request,'front.html')
    
def index(request):
    return render(request,'index.html')

def handleRegister(request):

    if request.method=='POST':
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1 != pass2:
            messages.error(request,'Password is incorrect')
            return render(request,'index.html')
            

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Register Successfull")
        return redirect('/login')
        
    return render(request,'index.html')   

def home(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return render(request,'login.html')
       
    return render(request,'home.html')




def contact(request):
    if request.method == "POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        desc=request.POST.get('desc','')
        if len(email)<4:
            messages.error(request,'Email is Invalid')
            return render(request,'contact.html')

        if len(phone)<10:
            messages.error(request,'Phone No is invalid')
            return render(request,'contact.html')

        if len(desc)<5:
            messages.error(request,'Description is invalid')
            return render(request,'contact.html')
        
        contact=Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()

        messages.success(request,"Your Response has been Recorded and Sent")

    return render(request,'contact.html')

def handleFlight(request):

    if request.method == "POST":

        roundtrip=request.POST.get('roundtrip')
        country=request.POST.get('country')
        country1=request.POST.get('country1')
        dept=request.POST.get('dept')
        retu=request.POST.get('retu')
        adult=request.POST.get('one')
        child=request.POST.get('two')
        travel=request.POST.get('three')
        register=Flight(roundtrip=roundtrip,country=country,country1=country1,dept=dept,retu=retu,adult=adult,child=child,travel=travel)
        register.save()
        messages.success(request,"BOOKING SUCCESSFUL OUR EMPLOYEE WILL GET BACK YOU SOON FOR MORE UPDATES")
        return redirect('/home')

      

    return render(request,'flight.html')

def about(request):
    return render(request,'about.html')

  
  



def handleLogin(request):
    if request.method=='POST':
        loginusername=request.POST['name']
        loginpassword=request.POST['pass1']
        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Login Successfull',)
            messages.warning(request,request.POST['name'])
            
            return render(request,'home.html') 
            return redirect('/home')
        else:
            messages.error(request,'Invalid Credentials')
            return render(request,'login.html')    


    return render(request,'login.html')    

def handleLogout(request):
    logout(request)
    messages.warning(request,"Successfully Logged Out")
    return redirect('/login')    

def show(request):
    query=request.GET['show']
    if len(query)>78:
        allPosts=Search.objects.none()
    else:
        allPostsTitle=Search.objects.filter(title_icontains=query)
        allPostsDate=Search.objects.filter
        # (content_icontains=query)
        allPosts=allPostsTitle.union(allPostsDate)

    if allPosts.count() == 0:
        messages.warning(request,"No Search Result")

    params={'allPosts':allPosts,'query':query}
    return render(request, 'show.html',params)