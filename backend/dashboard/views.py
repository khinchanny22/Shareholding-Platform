from django.contrib import messages
from django.contrib.auth import login, get_user_model, get_user
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission, Group
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Profile
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm


@login_required
def Dashboard(request):
    return render(request, 'backend/dashboard.html')


@login_required
def User(request):
    User = get_user_model()
    users = User.objects.order_by('-id')
    # pagination
    paginator = Paginator(users, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # user profile
    profile = Profile.objects.all()
    context = {
        'users': users,
        'page': page,
        'profile': profile
    }
    return render(request, 'backend/users/index.html', context)


@login_required
def ViewUserBackend(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    User = get_user_model()
    data = User.objects.get(id=id)

    context = {
        'data': data,
        'User': User,
    }
    return render(request, 'backend/users/profile.html', context)


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
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('User')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'backend/users/update.html', context)


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


# user group backend
@login_required
def UserGroupBackend(request):
    user_group = Group.objects.order_by('-id')
    paginator = Paginator(user_group, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'user_group': user_group,
        'page': page,
    }
    return render(request, 'backend/group_user/index.html', context)


# detail user group
def DetailUserGroup(request, id):
    obj = get_object_or_404(Group, id=id)
    context = {
        'obj': obj,
    }
    return render(request, 'backend/group_user/detail.html', context)
