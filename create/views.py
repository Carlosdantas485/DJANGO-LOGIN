from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.decorators import login_required

from .form import LoginForm
from .models import login

@login_required
def home(request):
    return render(request,'pages/home.html')

@login_required
def accounts(request): 
    Login_list =  login.objects.all()

    return render(request, 'pages/accounts.html', {'Login': Login_list})

@login_required
def ideaView(request, id):
    user = get_object_or_404(login, pk=id)
    return render(request, 'pages/InfoUser.html', {'user': user})

@login_required
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

@login_required
def editUser(request, id):
    InfoUser = get_object_or_404(login, pk=id)
    form = LoginForm(instance=InfoUser)

    if(request.method == 'POST'):
        form = LoginForm(request.POST, instance=InfoUser)

        if(form.is_valid()):
            InfoUser.save()
            return redirect('accounts')
        
        else:
            return render(request, 'pages/Editlogin.html', {'form': form, 'user': InfoUser})
        
            
    else:
        return render(request, 'pages/Editlogin.html', {'form': form, 'user': InfoUser})

@login_required
def deleteUser(request,id):
    InfoUser = get_object_or_404(login, pk=id)
    InfoUser.delete()
    return redirect('accounts')

