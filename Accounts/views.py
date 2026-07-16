from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import auth

from Accounts.forms import RegisterForm

# Create your views here.
def register(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
     form.save()
     return redirect('login_view')
    
  context = {
    'form': form,
  }
  return render(request, 'Accounts/register.html', context)

def login_view(request):  # Renamed from 'login' to prevent conflicts
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
               auth.login(request, user)
               return redirect('dashboard')  # Use URL name, not the HTML filename
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'Accounts/login_view.html', context)
  
def logout(request):
   auth.logout(request)
   return redirect('blog_homepage')