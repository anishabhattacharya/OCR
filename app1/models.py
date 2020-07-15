from django.db import models
import datetime

class Course(models.Model):
    name=models.CharField(max_length=60,unique=True)
    faculty=models.CharField(max_length=60)
    date=models.DateField()
    time=models.TimeField(auto_now=False,auto_now_add=True)
    fee=models.FloatField()
    duration=models.IntegerField()



class Student(models.Model):
    name=models.CharField(max_length=50,unique=True)
    contactno=models.IntegerField(unique=True)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=10)
