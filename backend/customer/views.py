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
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = CustomerForm(request.POST, request.FILES)

        # In the 'form' class the clean function
        # is defined, if all the data is correct
        # as per the clean function, it returns true
        if details.is_valid():

            # Temporarily make an object to be add some
            # logic into the data if there is such a need
            # before writing to the database
            post = details.save(commit=False)

            # Finally write the changes into database
            post.save()
            messages.success(request, 'Data Customer Successful!')
            # redirect it to some another page indicating data
            # was inserted successfully
            return redirect('Customers')

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "backend/customers/create.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = CustomerForm(None)
        # return render(request, 'home.html', {'form': form})
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
