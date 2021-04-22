from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'pages/home.html')

def register(request): 
    return render(request, 'pages/register.html')

def accounts(request): 
    return render(request, 'pages/accounts.html')
