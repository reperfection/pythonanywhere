from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogModelForm

def index(request):
	posts = Blog.objects.all()
	return render(request, 'index.html', {'posts':posts})

def create(request):
    if request.method == 'POST':
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BlogModelForm()
    return render(request, 'create.html', {'form':form})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog_detail':blog_detail})