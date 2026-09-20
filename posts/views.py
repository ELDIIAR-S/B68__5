from django.shortcuts import render, redirect, get_object_or_404

from .forms import PostForm
from .models import Post


def list_posts(request):
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'posts/list_posts.html', context)


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('posts:list_posts')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'posts/create_post.html', context)


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('posts:list_posts')

    context = {
        'post': post,
    }

    return render(request, 'posts/post_delete.html', context)