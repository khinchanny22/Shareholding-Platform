from django.contrib.auth import forms
from django.contrib import messages
from django.contrib.auth import login, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


@login_required
def Dashboard(request):
    return render(request, 'backend/dashboard.html')


@login_required
def User(request):
    User = get_user_model()
    users = User.objects.order_by('-id')
    paginator = Paginator(users, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    data = {
        'users': users,
        'page': page
    }
    return render(request, 'backend/users/index.html', data)


@login_required
def ViewUserManagement(request):
    pass


@login_required
def CreateUserBackend(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('User')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = CustomUserCreationForm()
    return render(request=request, template_name="backend/users/create.html", context={"form": form})


# function Update Users Backend
@login_required
def UpdateUsersBackend(request):
    return render(request, 'backend/users/update.html')

@login_required
def UserPermission(request):
    permissions = Permission.objects.order_by('-id')
    paginator = Paginator(permissions, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'permission': permissions,
        'page': page,
    }
    return render(request, 'backend/permission/index.html', context)
