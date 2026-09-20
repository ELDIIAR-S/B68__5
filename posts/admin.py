from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

# from django.contrib import admin

# from posts.models import Post

# # Register your models here.

# admin.site.register(Post)
