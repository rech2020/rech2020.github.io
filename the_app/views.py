from django.shortcuts import render, redirect
from the_app.models import *
from the_app.forms import *
from django.views.generic import DeleteView
# Create your views here.

def about(request):
    return render(request, 'the_app/about.html')

def contact(request):
    return render(request, 'the_app/contact.html')

def posts(request):
    bd = list(Post.objects.all())
    return render(request, 'the_app/home.html', {'posts':bd})

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/')
    form = PostForm
    data = {
        'form': form
    }
    return render(request, 'the_app/create.html', data)

def edit(request):
    post = Post.objects.get(pk=3)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post.save()
            return redirect('home')
    form = PostForm()
    return render(request, 'the_app/change.html', {'form': form})

class delete(DeleteView):
    model = Post
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'the_app/delete.html'

def fake_delete(request):
    return render(request, 'the_app/fake_delete.html')