from django.shortcuts import redirect, render, HttpResponse
from django.http.response import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from project.models import *
def home(request):
    posts=Blog.objects.all()
    context={"posts":posts}
    return render(request,"index.html",context)

def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')

        if pass1!=pass2:
            messages.warning(request,'Password is not matching')
            return redirect('/signup')

        try:
            if User.objects.get(username=username):
                messages.warning(request,"username is already taken")
                return redirect('/signup')
        except Exception as Identifier:
            pass

        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is already taken")
                return redirect('/signup')
        except Exception as Identifier:
            pass

        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    return render(request,"signup.html")
def handlelogin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        myuser=authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,'Login Successfull')
            return redirect('/blog')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"login.html")
def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully Logged Out')
    return redirect('/login')
def blog(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            title=request.POST.get('title')
            description=request.POST.get('description')
            img_url=request.POST.get('url')
            category=request.POST.get('category')
            print(category)
            if(title==None or description==None or img_url==None):
                messages.info(request,"Please enter correct values")
                return render(request,"blog.html")
            myquery=Blog(username=request.user,title=title,description=description,img_url=img_url,blog_category=category)
            myquery.save()
            messages.info(request,"Your blog is added")
        return render(request,"blog.html")
    return redirect("/login")
def contact(request):
    if request.user.is_authenticated:
        if request.method=="POST":
            subject=request.POST.get('subject')
            description=request.POST.get('description')
            number=request.POST.get('number')
            myquery=Contact(username=request.user,subject=subject,description=description,contact_number=int(number))
            myquery.save()
            messages.info(request,"Thank you for Contacting Us. We will get back to you soon.")
        return render(request,"contact.html")
    return redirect("/login")
def singleblog(request,id):
    id=int(id)
    posts=Blog.objects.filter(id=id)
    context={"posts":posts}
    return render(request,"singleblog.html",context)
def categoryblogs(request,category):
    posts=Blog.objects.filter(blog_category=category)
    context={"posts":posts,"category":category}
    return render(request,"categoryblogs.html",context)
# Create your views here.
