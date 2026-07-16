from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from blog.models import Blog, Category
from .forms import AddUserForm, BlogsForm, CategoryForm, EditUserForm


# Create your views here.
@login_required(login_url='login_view')
def dashboard(request):
  category_count = Category.objects.all().count()
  blogs_count = Blog.objects.all().count()
  
  context = {
    'category_count': category_count,
    'blogs_count': blogs_count,
  }
  return render (request, 'dashboard/dashboard.html', context)

def categories(request):
  return render(request, 'dashboard/categories.html')

def create_category(request):
  form = CategoryForm()

  if request.method == 'POST':
    form = CategoryForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('categories')
    
  context = {
    'form': form,
  }  
  return render(request, 'dashboard/create_category.html', context)

def edit_category(request, pk):
  category = get_object_or_404(Category, pk=pk)

  if request.method == 'POST':
    form = CategoryForm(request.POST, instance=category)
    if form.is_valid():
      form.save()
      return redirect('categories')

  else:
    form = CategoryForm(instance=category)

  context = {
   'form': form,
   'category': category,
  }
  return render(request, 'dashboard/edit_category.html', context)

@login_required(login_url='login_view')
def delete_category(request, pk):
  category = get_object_or_404(Category, pk=pk)

  if request.method == 'POST':
    category.delete()
    return redirect('categories')

  context = {
    'category': category,
  }
  return render(request, 'dashboard/delete_category.html', context)

def blogs(request):
  blogs = Blog.objects.all()

  context = {
    'blogs': blogs,
  }
  return render(request, 'dashboard/blogs.html', context)

@login_required
def add_blog(request):
    form = BlogsForm()

    if request.method == "POST":
        form = BlogsForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("blogs_list")

    return render(request, "dashboard/add_blog.html", {"form": form})

def edit_blog(request, pk):
  blog = get_object_or_404(Blog, pk=pk)

  if request.method == 'POST':
    form = BlogsForm(request.POST, request.FILES, instance=blog,)
    if form.is_valid():
      form.save()
      return redirect('blogs_list')
    
  else:
   form = BlogsForm(instance=blog)

  context = {
    'form': form,
    'blog': blog,
  }
  return render(request, 'dashboard/edit_blog.html', context)

def delete_blog(request, pk):
  blog = get_object_or_404(Blog, pk=pk)

  if request.method == 'POST':
    blog.delete()
    return redirect('blogs_list')

  context = {
    'blog': blog,
  }
  return render(request, 'dashboard/delete_blog.html', context)

#def logout(request):
  return render(request, 'dashboard/logout.html')

def users(request):
  users = User.objects.all()

  context = {
    'users': users,
  }
  return render(request, 'dashboard/users.html', context)

# ADDING USERS TO THE BACKEND
def add_user(request):
  if request.method == 'POST':
    form = AddUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('users')
  else:
    form = AddUserForm()

  context = {
    'form': form,
  }
  return render(request, 'dashboard/add_user.html', context)

def edit_user(request, pk):
  user = get_object_or_404(User, pk=pk)
  if request.method == 'POST':
    form = EditUserForm(request.POST, instance=user,)
    if form.is_valid():
      form.save()
      return redirect('users')
    
  else:
   form = EditUserForm(instance=user)

  context = {
    'form': form,
  }
  return render(request, 'dashboard/edit_user.html', context)

def delete_user(request, pk):
  user = get_object_or_404(User, pk=pk)
  if request.method == 'POST':
    user.delete()
    return redirect('users')

  context = {
    'user': user,
  }
  return render(request, 'dashboard/delete_user.html', context)