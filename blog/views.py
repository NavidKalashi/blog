from django.shortcuts import render, redirect

from .models import Post, Tag
from .forms import CustomPostForm

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

def addBlog(request):
    if request.method == 'POST':
        form = CustomPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blogs')
    else:
        form = CustomPostForm()
    context = {'form': form}
    return render(request, 'blog/add-blog.html', context)