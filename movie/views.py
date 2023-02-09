from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    #return render(request,'home.html')
    return render(request,'home.html',{'name':'Samuel Oviedo'})

def about(request):
    #return render(request,'home.html')
    return HttpResponse('<h1>Welcome to About page</h1>')


# Create your views here.
