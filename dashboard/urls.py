from django.urls import path
from dashboard import views

urlpatterns = [
  path('', views.dashboard, name='dashboard'),
  path('categories/', views.categories, name='categories'),
  path('create_category/', views.create_category, name='create_category'),
  path('edit_category/<int:pk>/', views.edit_category, name='edit_category'),
  path('delete/<int:pk>/', views.delete_category, name='delete_category'),

  #POSTS URLS DONE HERE
  path('blogs/', views.blogs, name='blogs_list'),
  path('add_blog/', views.add_blog, name='add_blog'),
  path('edit_blog/<int:pk>/', views.edit_blog, name='edit_blog'),
  path('delete_blog/<int:pk>/', views.delete_blog, name='delete_blog'),

]