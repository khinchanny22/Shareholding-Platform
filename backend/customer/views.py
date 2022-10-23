from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CustomerForm
from .models import Customer

# Create your views here.



def Customers(request):
    data = Customer.objects.order_by('-id')

    content = {
        'data': data,
    }
    return render(request, 'backend/customers/index.html', content)


def AddCustomers(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('Customers')
            except:
                pass
    else:
        form = CustomerForm()
    return render(request, 'backend/customers/create.html', {'form': form})


def UpdateCustomer(request, id):
    context = {}

    obj = get_object_or_404(Customer, id=id)

    form = CustomerForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('Customers')

    context["form"] = form
    return render(request, 'backend/customers/update.html', context)





