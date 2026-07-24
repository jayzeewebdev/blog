from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from Bioblog.models import About, Social_media_links
from blog.forms import CommentForm
from blog.models import Blog, Category
from blog.models import Comment


# Create your views here.
def homepage(request):
  featured_posts = Blog.objects.filter(is_featured=True).order_by('-created_at')
  headlines = Blog.objects.filter(is_headlines = True)
  posts = Blog.objects.filter(is_featured = False)
  about = About.objects.get()
  #links = Social_media_links.objects.all()
  context = {
    'featured_posts':featured_posts,
    'posts': posts,
    'headlines': headlines,
    'about': about,
    #'links': links
  }
  return render(request, 'homepage.html', context)

def posts_by_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Blog.objects.filter(category=category)  # or category.posts.all()
    context = {
       'category': category,
       'posts': posts,
    }
    return render(request, 'blog/posts_by_category.html', context)

def post_detail_page(request, slug):
   post = get_object_or_404(Blog, slug=slug)
   comments = post.comment_set.all()

   context = {
      'post': post,
      'comments': comments,
   }
   return render(request, 'blog/post_detail_page.html', context)

def search(request):
   keyword = request.GET.get('keyword')
   blogs = Blog.objects.filter(Q(title__icontains=keyword)|Q(short_description__icontains=keyword)|Q(blog_body__icontains=keyword))
  
   context = {
      'blogs': blogs,
      'keyword': keyword,
   }
   return render(request, 'search.html', context)

@login_required
def add_comment(request, slug):
    post = get_object_or_404(Blog, slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = post
            comment.save()
            return redirect('post_detail_page', slug=post.slug)
    else:
        form = CommentForm()

    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'blog/add_comment.html', context)

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Comment       # <-- Make sure you import the Comment MODEL
from .forms import CommentForm    # <-- Make sure you import the Comment FORM

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail_page', slug=comment.blog.slug)
    else:
        form = CommentForm(instance=comment)

    context = {
        'comment': comment,
        'form': form,
    }
    return render(request, 'blog/edit_comment.html', context)

def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)

    if request.method == 'POST':
        blog_slug = comment.blog.slug   # grab this before deleting
        comment.delete()
        return redirect('post_detail_page', slug=blog_slug)

    context = {
        'comment': comment,
    }
    return render(request, 'blog/delete_comment.html', context)