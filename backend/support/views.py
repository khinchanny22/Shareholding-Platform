from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import *
from .models import Policy


@login_required
def IndexSupportFrontend(request):
    policy = Policy.objects.order_by('-id')
    paginator = Paginator(policy, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'policy': policy,
        'page': page,
    }
    return render(request, 'backend/support/index.html', context)


# ViewsPolicy
@login_required
def ViewsPolicy(request, id):
    views = get_object_or_404(Policy, id=id)
    context = {
        'views': views,
    }
    return render(request, 'backend/support/views.html', context)


@login_required
def CreatePolicy(request):
    form = SupportAdminForm()
    if request.method == "POST":
        form = SupportAdminForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('IndexSupportFrontend')
            except:
                message = "Something we are wrong!"
                form = SupportAdminForm()
            return render(request, 'backend/support/create.html', {'message': message, 'form': form})
    else:
        form = SupportAdminForm()
        return render(request, 'backend/support/create.html', {'form': form})


@login_required
def UpdatePolicy(request, id):
    term = Policy.objects.get(id=id)
    if request.method == "POST":
        form = SupportAdminForm(request.POST, request.FILES, instance=term)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("IndexSupportFrontend")
        message = 'Something we are wrong!'
        return render(request, 'backend/support/update.html', {'message': message, 'term': form})
    else:
        form = Policy.objects.get(id=id)
        term = SupportAdminForm(instance=form)
        context = {'term': term, 'id': id}
        return render(request, 'backend/support/update.html', context)


# IndexTermCondition
@login_required
def IndexTermCondition(request):
    users = TermCondition.objects.order_by('-id')
    # pagination
    paginator = Paginator(users, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    context = {
        'users': users,
        'page': page,
    }
    return render(request, 'backend/term-condition/index.html', context)


@login_required
def AddTermCondition(request):
    form = TermConditionForm()
    if request.method == "POST":
        form = TermConditionForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Created successful!")
                return redirect('IndexTermCondition')
            except:
                message = "Something we are wrong!"
                form = TermConditionForm()
            return render(request, 'backend/term-condition/create.html', {'message': message, 'form': form})
    else:
        form = TermConditionForm()
    return render(request, 'backend/term-condition/create.html', {'form': form})


@login_required
def UpdateTermCondition(request, id):
    term = TermCondition.objects.get(id=id)
    if request.method == "POST":
        form = TermConditionForm(request.POST, request.FILES, instance=term)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("IndexTermCondition")
        message = 'Something we are wrong!'
        return render(request, 'backend/term-condition/update.html', {'message': message, 'term': form})
    else:
        form = TermCondition.objects.get(id=id)
        term = TermConditionForm(instance=form)
        context = {'term': term, 'id': id}
    return render(request, 'backend/term-condition/update.html', context)


def ViewsTermCondition(request, id):
    views = get_object_or_404(TermCondition, id=id)
    context = {
        'views': views,
    }
    return render(request, 'backend/term-condition/views.html', context)


def DeleteTermCondition(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(TermCondition, id=id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("IndexTermCondition")

    return render(request, "backend/term-condition/delete.html", context)
