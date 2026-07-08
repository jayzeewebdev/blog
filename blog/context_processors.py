
from Bioblog.models import Social_media_links
from blog.models import Category


def get_categories(request):
  categories = Category.objects.all()
  return dict(categories=categories)

def get_social_links(request):
  links = Social_media_links.objects.all()
  return dict(links=links)