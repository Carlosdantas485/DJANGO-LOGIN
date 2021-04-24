from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .form import LoginForm

from .models import login

def home(request):
    return render(request,'pages/home.html')

def accounts(request): 
        Login =  login.objects.all()
        return render(request, 'pages/accounts.html', {'Login': Login})

def loginView(request, id):
    Login = get_object_or_404(login, pk=id)
    return render(request, 'pages/login.html', {'Login': Login})

def register(request): 
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            login = form.save(commit=False)
            login.done = 'doing'
            login.save()
            return redirect('/')

    else:
        form = LoginForm()
        return render(request, 'pages/register.html', {'form': form})

def editLogin(request, id):
    Login = get_object_or_404(login, pk=id)
    form = LoginForm(instance=login)

    if(request.method == 'POST'):
        return False
    else:
        return render(request, 'pages/EditLogin.html', {'form': form, 'Login': Login})



