from django.db import models

# Create your models here.

from django.utils import timezone

class Emp(models.Model):
       eid = models.CharField(max_length=10)
       ename=models.CharField(max_length=24)
       eadd = models.TextField()
       dob = models.DateTimeField(default = timezone.now())

class Student(models.Model):
       Sid =  models.CharField(max_length=10)
       Sname= models.CharField(max_length=24)
       