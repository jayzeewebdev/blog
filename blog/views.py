from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.db.models import Q


from Bioblog.models import About, Social_media_links
from blog.models import Blog, Category, Comment

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
   if request.method == 'POST':
      comment = Comment()
      comment.user = request.user
      comment.blog = post
      comment.comment = request.POST['comment']
      comment.save()
      return HttpResponseRedirect(request.path_info)

   comments = Comment.objects.filter(blog=post)
   comment_count = comments.count()

   context = {
      'post': post,
      'comments': comments,
      'comment_count': comment_count,
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