from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import Course,Student

def ShowIndex(request):
    return render(request,"index.html")

def adminLogin(request):
    return render(request,"admin_login.html")


def adminloginCheck(request):
    uname=request.POST.get('t1')
    pwd=request.POST.get('t2')
    if uname == "anisha" and pwd == "bhat@1234":
        return redirect('admin_welcome')
    else:
        messages.error(request,"Invalid username and password")
        return redirect('admin_login')


def adminWelcome(request):
    return render(request,"admin_welcome.html")

def add_classes(request):
    return render(request,"schedule_class.html")


def view_classes(request):
    result = Course.objects.all()
    return render(request,"view_scheduled.html",{"data":result})

def save_courses(request):
    name = request.POST.get("t1")
    faculty = request.POST.get("t2")
    date = request.POST.get("t3")
    time = request.POST.get("t4")
    fee = request.POST.get("t5")
    duration=request.POST.get("t6")
    Course(name=name, faculty=faculty, date=date, time=time, fee=fee, duration=duration).save()
    return redirect('view_courses')

def main(request):
    return render(request,"main.html")




