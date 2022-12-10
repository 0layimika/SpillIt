from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import blog
from django.utils import timezone
def home(request):
    blogs = blog.objects
    return render(request, 'blogs/home.html', {'blogs': blogs})


@login_required(login_url='/account/signup')
def create(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['body'] and request.FILES['image']:
            Blog = blog()
            Blog.title = request.POST['title']
            Blog.body = request.POST['body']
            Blog.image = request.FILES['image']
            Blog.pub_date = timezone.datetime.now()
            Blog.publisher = request.user
            Blog.save()
            return redirect('/blog/' + str(Blog.id))
        else:
            return render(request, 'blogs/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'blogs/create.html')

def detail(request, Blog_id):
    Blog = get_object_or_404(blog, pk=Blog_id)
    return render(request, 'blogs/detail.html',{'blog':Blog})


@login_required(login_url='/account/signup')
def like(request, Blog_id):
    if request.method == 'POST':
        Blog = get_object_or_404(blog, pk=Blog_id)
        Blog.like += 1
        Blog.save()
        return redirect('/blog/' + str(Blog.id))


# Create your views here.
