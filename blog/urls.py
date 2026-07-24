from django.urls import path

from . import views

urlpatterns = [
  path('', views.homepage, name='blog_homepage'),
  path('posts_by_category/<int:pk>/', views.posts_by_category, name='posts_by_category'),
  path('posts/<slug:slug>/', views.post_detail_page, name='post_detail_page'),

  # search feature endpoint here
  path('blog/search/', views.search, name='search'),

  path('add_comment/<slug:slug>/', views.add_comment, name='add_comment'),
  path('edit_comment/<int:pk>/', views.edit_comment, name='edit_comment'),
  path('delete/<int:pk>/', views.delete_comment, name='delete_comment'),
]