from django.contrib import admin

from .models import Blog, Category

# configurations of admin in the background is done here
class BlogAdmin(admin.ModelAdmin):
  prepopulated_fields = {'slug': ('title',)}
  list_display = ('title', 'category', 'author', 'status', 'is_featured', 'is_headlines',)
  list_editable = ('is_featured', 'is_headlines',)
  search_fields = ('status', 'title', 'category__category_name', 'id',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)