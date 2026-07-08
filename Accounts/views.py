from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login

from Accounts.forms import RegisterForm

# Create your views here.
def register(request):
  form = RegisterForm()

  if request.method == 'POST':
    form = RegisterForm(request.POST)
    if form.is_valid():
     form.save()
  context = {
    'form': form,
  }
  return render(request, 'Accounts/register.html', context)

def login_view(request):  # Renamed from 'login' to prevent conflicts
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('blog_homepage')  # Use URL name, not the HTML filename
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'Accounts/login_view.html', context)
  
