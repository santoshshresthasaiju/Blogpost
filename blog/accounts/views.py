from django.shortcuts import render, redirect
from .forms import CreateForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

def register_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CreateForm()
    return render(request, 'accounts/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blogpost:home')
        else:
            return render(request, 'accounts/login.html', {'form':form})
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})
    
@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    return redirect('login')
    
