from django.db import models

# Create your models here.
class About(models.Model):
  about_heading = models.CharField(max_length=100, blank=True, null=True)
  about_description = models.CharField(max_length=10000, default='about me')
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
        # Always return a string, even if heading is missing
        return self.about_heading if self.about_heading else "About Section"

  class Meta:
    verbose_name_plural = 'About'

class Social_media_links(models.Model):
  social_media_name = models.CharField(max_length=100)
  social_media_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
  link = models.URLField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = 'Social Media'

  def __str__(self):
    return self.social_media_name