from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Hello(request):
    return HttpResponse("Welcome to Resh world")
from ReshApp.forms import Emp

def show(request):
    form = Emp
    return render(request , 'student.html' , {'f':form})

def showdetails(request):
	form = studentmodelform()
	return render(request, 'student.html', {'form':form})
