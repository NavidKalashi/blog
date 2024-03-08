from django.shortcuts import render

from .models import Post

def index(request):
    return render(request, 'index.html')

def blogs(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blogs.html', context)

def blog(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'blog/blog.html', context)