from django.shortcuts import render,redirect
from django.contrib import messages
from app1.models import Course,Student,EnrolledStudents
from django.db import IntegrityError

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
    return redirect('add_classes')

def main(request):
    return render(request,"main.html")

def register_student(request):
    return render(request,"student_registration.html")

def view_register(request):
    res = Student.objects.all()
    return render(request,"view_register.html")


def save_info(request):
    name=request.POST.get("s1")
    contactno=request.POST.get("s2")
    email=request.POST.get("s3")
    password=request.POST.get("s4")
    print(password)
    Student(name=name, contactno=contactno, email=email, password=password).save()
    return redirect('main')

#def view_register(request):
    #res = Student.objects.all()
    #return render(request,"view_register.html")



def studentLogin(request):
    return render(request,"student_login.html")


def studentloginCheck(request):
    un=request.POST.get('u1')
    pas=request.POST.get('u2')
    print(un,pas)
    usr = Student.objects.filter(email =un)
    print(usr)
    for x in usr:
        if pas==x.password:
            return render(request,"welcome_student.html")
    messages.error(request,"invalid user")
    return redirect('student_login')

def welcome_student(request):
    return render(request, "welcome_student.html")

def enroll_students(request):
    return render(request,"enroll_students.html")

def view_enrolledcourse(request):
    return render(request,"view_enrolledcourse.html")
