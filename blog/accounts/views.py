from django.shortcuts import render, redirect
from .forms import CreateForm, LoginForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# views for register 
def register_view(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = CreateForm()
    return render(request, 'accounts/register.html', {'form':form})

# views for login
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('blogpost:home')
        else:
            messages.error(request, 'Invalid username or password.') 
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form':form})

# views for logout
@login_required(login_url='login')
def logout_view(request):
    auth.logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('login')
    
