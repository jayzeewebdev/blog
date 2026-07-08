from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  role = models.CharField(
    max_length=50,
    choices=[
      ('AUTHOR', 'Author'),
      ('EDITOR', 'Editor'),
      ('SUPERUSER', 'Superuser'),
    ],
    default='AUTHOR'
    )
  bio = models.TextField(blank=True)
  user_profile_image = models.ImageField(upload_to='profiles/', blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.user.username