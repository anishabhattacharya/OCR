"""OCR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.ShowIndex,name="main"),
    path('admin_login/',views.adminLogin,name="admin_login"),
    path('admin_login_check/',views.adminloginCheck,name="admin_login_check"),
    path('admin_welcome/',views.adminWelcome,name="admin_welcome"),
    path('add_classes/',views.add_classes,name="add_classes"),
    path('view_classes/',views.view_classes,name="view_classes"),
    path('save_courses/',views.save_courses,name="save_courses"),
    path('main/',views.main,name="main"),
    path('register_student/',views.register_student,name="register_student"),
    path('view_register/',views.view_register,name="view_register"),
    path('save_info/',views.save_info,name="save_info"),
    path('student_login/',views.studentLogin,name="student_login"),
    path('student_login_check/',views.studentloginCheck,name="student_login_check"),

]
