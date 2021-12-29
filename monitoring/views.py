from django.shortcuts import render
from django.http import HttpResponse
from .models import mydb

# Create your views here.
    
def welcome(request):
    return render(request,'Welcome-To-Our-Service.html')

def welcome1(request):
    return render(request,'home.html')
    #tutorial webpage
def tutorial(request):
    return render(request,'Tuto.html')
    #for tempsensor web page
def mydb1(request):
    tab = mydb.objects.all()
    s = {'tab': tab}
    return render(request,'TEMP-SENSOR.html', s)
    

def mydb2(request):
    tab = mydb.objects.all()
    s= {'tab':tab}    
    return render(request,'Temp.html',s)

