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
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Add successful!')
            return redirect('Customers')
    else:
        form = CustomerForm()
    return render(request, 'backend/customers/create.html', {'form': form})


@login_required
def UpdateCustomer(request, id):
    context = {}

    obj = get_object_or_404(Customer, id=id)

    form = CustomerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('Customers')

    context["form"] = form
    return render(request, 'backend/customers/update.html', context)
