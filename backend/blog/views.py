from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .forms import BlogForm
from .models import PostBlog


def IndexPostBlog(request):
    post_blog = PostBlog.objects.order_by('-id')
    paginator = Paginator(post_blog, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'post_blog': post_blog,
        'page': page,
    }

    return render(request, 'backend/blog/index_blog_post.html', content)


def AddPostBlog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect('IndexPostBlog')
    else:
        form = BlogForm()
    return render(request, 'backend/blog/create.html', {'form': form})


def UpdateBlogPost(request, id):
    post_blog = PostBlog.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=post_blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("IndexPostBlog")
        message = 'Something we are wrong!'
        return render(request, 'backend/blog/update_blog_post.html', {'message': message, 'post_blog': form})
    else:
        form = PostBlog.objects.get(id=id)
        post_blog = BlogForm(instance=form)
        content = {'post_blog': post_blog, 'id': id}
    return render(request, 'backend/blog/update_blog_post.html', content)


# blog Post frontend side
def IndexBlogFrontend(request):
    post_blog_frontend = PostBlog.objects.order_by('-id')
    paginator = Paginator(post_blog_frontend, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'post_blog_frontend': post_blog_frontend,
        'page': page,
    }
    return render(request, 'frontend/blog/frontend_post_blog.html', content)


# RecentPostProduct
def RecentPostProduct(request):
    recent = PostBlog.objects.order_by('-id')
    paginator = Paginator(recent, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'recent': recent,
        'page': page,
    }
    return render(request, 'frontend/blog/frontend_post_blog.html', content)


# PopularPostProduct
def PopularPostProduct(request):
    popular = PostBlog.objects.all()
    return HttpResponse(popular)
    exit()
    paginator = Paginator(popular, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'popular': popular,
        'page': page,
    }
    return render(request, 'frontend/blog/frontend_post_blog.html', content)
