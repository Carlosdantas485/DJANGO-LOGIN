from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import login

def home(request):
    return render(request,'pages/home.html')

def register(request): 
    return render(request, 'pages/register.html')

def accounts(request): 

    Login =  login.objects.all()
    return render(request, 'pages/accounts.html', {'Login': Login})

def loginview(request, id):
    Login = get_object_or_404(login, pk=id)
    return render(request, 'pages/login.html', {'login': Login})