from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
  category_name = models.CharField(max_length=50, unique=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'Categories'

  def __str__(self):
    return self.category_name

from django.utils.text import slugify

class Blog(models.Model):
    STATUS_CHOICES = [
        (0, 'Draft'),
        (1, 'Published')
    ]

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    short_description = models.TextField(max_length=1000)
    blog_body = models.TextField(max_length=10000)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    is_headlines = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogs'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while Blog.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

class Comment(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
   comment = models.TextField(max_length=300)
   created_at = models.DateTimeField(auto_now_add=True)
   update_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.comment

