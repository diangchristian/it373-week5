from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from django.contrib import messages
from pages.models import Post
from pages.forms import PostForm

# Create your views here.

def home(request):
    
    context = {
        'title': 'Home',
        'features': ['Django', 'Templates', 'Static Files'
                    
                     ],
    }
    
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {'title' : 'About'})


def hello(request, name):
    return render(request, 'hello.html', {'name': name})


def gallery(request):
    images = ['img1.jpg', 'img2.jpg', 'img3.jpg']
    return render(request, 'gallery.html', {'images' : images})


def page_not_found_view (request, exception):
    return render(request, '404.html', status=404)


def server_error_view (request, exception):
      return render(request, '500.html', status=500)
  
def post_list(request):
    posts = Post.objects.all().prefetch_related('comments')
    return render(request, 'post_list.html', {'posts': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New post created')
            return redirect('post_list')
        messages.error(request,'Please correct the errors below')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})


def post_view(request, pk):
    # post = get_object_or_404(Post, pk=pk)
    post = Post.objects.get(pk=pk)
    return render(request, 'post_view.html', {'post': post})


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,'Post updated')
            return redirect('post_view', pk=pk)
        messages.error(request,'Please correct the errors below')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request,f"Post '{post.title}' deleted")
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'post': post})
