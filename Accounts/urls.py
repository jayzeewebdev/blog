from django.urls import path

from Accounts import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login_view/', views.login_view, name='login_view'),
]