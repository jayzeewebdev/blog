from django.urls import path
from dashboard import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', views.categories, name='categories'),
  path('create_category/', views.create_category, name='create_category'),
  path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
  path('delete/<int:pk>/', views.delete_category, name='delete_category'),
]