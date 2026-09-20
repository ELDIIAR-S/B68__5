from django.urls import path
from . import views


app_name = 'posts'

urlpatterns = [
    path('', views.list_posts, name='list_posts'),
    path('create/', views.create_post, name='create_post'),
    path('delete/<int:post_id>/', views.post_delete, name='post_delete'),
]