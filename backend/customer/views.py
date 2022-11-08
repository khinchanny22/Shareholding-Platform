from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomerForm
from .models import Customer


# Create your views here.

@login_required
def Customers(request):
    data = Customer.objects.order_by('-id')
    paginator = Paginator(data, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'data': data,
        'page': page,
    }
    return render(request, 'backend/customers/index.html', content)


@login_required
def AddCustomersBackend(request):
    if request.method == 'POST':
        details = CustomerForm(request.POST, request.FILES)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            messages.success(request, 'Data Created Successful!')
            return redirect('Customers')
        else:
            return render(request, 'backend/customers/create.html', {'form': details})
    else:
        form = CustomerForm(None)
    return render(request, 'backend/customers/create.html', {'form': form})


@login_required
def UpdateCustomerBackend(request, id):
    update_customer = Customer.objects.get(id=id)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=update_customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("Customers")
        message = 'Something we are wrong!'
        return render(request, 'backend/customers/update.html', {'message': message, 'update_customer': form})
    else:
        form = Customer.objects.get(id=id)
        update_customer = CustomerForm(instance=form)
        context = {'update_customer': update_customer, 'id': id}
    return render(request, 'backend/customers/update.html', context)


@login_required
def ViewCustomerBackend(request, id):
    views_customer = get_object_or_404(Customer, id=id)
    context = {
        'views_customer': views_customer,
    }
    return render(request, 'backend/customers/view.html', context)


# customers register users
# function customers register user
def RegisterCustomerFrontend(request):
    if request.method == 'POST':
        details = CustomerForm(request.POST, request.FILES)
        if details.is_valid():
            post = details.save(commit=False)
            post.save()
            messages.success(request, 'Data Created Successful!')
            return redirect('frontend')
        else:
            return render(request, 'frontend/customers/register.html', {'form': details})
    else:
        form = CustomerForm(None)
    return render(request, 'frontend/customers/register.html', {'form':form})
