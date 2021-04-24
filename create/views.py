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
    user = get_object_or_404(login, pk=id)
    return render(request, 'pages/login.html', {'user': user})

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

def editUser(request, id):
    InfoUser = get_object_or_404(login, pk=id)
    form = LoginForm(instance=InfoUser)

    if(request.method == 'POST'):
        return False
    else:
        return render(request, 'pages/Editlogin.html', {'form': form, 'user': InfoUser})



