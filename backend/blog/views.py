from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator

from .forms import BlogForm, BlogCommentForm
from .models import PostBlog


@login_required
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


@login_required
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


@login_required
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


# function Views or Details block Backend
@login_required
def ViewPostblogBackend(request, id):
    data = get_object_or_404(PostBlog, id=id)
    return render(request, 'backend/blog/view_post_blog_backend.html', {'data': data})


# starting function
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


# ViewsBlogFrontend
def ViewsBlogFrontend(request, id):
    data = get_object_or_404(PostBlog, id=id)
    # recent
    recent = PostBlog.objects.order_by('-id')
    # popular
    popular = PostBlog.objects.filter()
    # add comment blog frontend
    if request.method == 'POST':
        form = BlogCommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add Comment Successful!')
            return redirect('ViewsBlogFrontend')
    else:
        form = BlogCommentForm()
    # end comment blog frontend
    paginator = Paginator(recent, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        "data": data,
        "recent": recent,
        "page": page,
        "popular": popular,
        "form": form
    }
    return render(request, 'frontend/blog/frontend_post_views.html', context)


# RecentPostProduct
@login_required
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
@login_required
def PopularPostProduct(request):
    popular = PostBlog.objects.all()
    paginator = Paginator(popular, 5)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'popular': popular,
        'page': page,
    }
    return render(request, 'frontend/blog/frontend_post_blog.html', content)
