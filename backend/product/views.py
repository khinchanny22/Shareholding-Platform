
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from .forms import ProductForm, ProductPriceForm, PostForm
from .models import *


# start product backend
# function product index backend
@login_required
def IndexProductBackend(request):
    product = Product.objects.order_by('-id')
    paginator = Paginator(product, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'product': product,
        'page': page,
    }
    return render(request, 'backend/product/index.html', content)


# add product backend
@login_required
def AddProductBackend(request):
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = ProductForm(request.POST, request.FILES)

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
            messages.success(request, 'Data Product successful!')
            # redirect it to some another page indicating data
            # was inserted successfully
            return redirect('IndexProductBackend')

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "backend/product/create.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = ProductForm(None)
        # return render(request, 'home.html', {'form': form})
        return render(request, 'backend/product/create.html', {'form': form})


# Update Product Backend
@login_required
def UpdateProductBackend(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Product, id=id)
    # pass the object as instance in form
    form = ProductForm(request.POST or None, instance=obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.success(request, 'Update Product successful!')
        return redirect("IndexProductBackend")
    # add form dictionary to context
    context["form"] = form
    return render(request, 'backend/product/update.html', {'form': form})


# view Product Backend
@login_required
def ViewProductBackend(request, id):
    data = get_object_or_404(Product, id=id)
    return render(request, 'backend/product/view.html', {'data':data})


# start Product Cost Backend
@login_required
def ProductCost(request):
    product = ProductPrice.objects.order_by('-id')
    data = {'product': product, }
    return render(request, 'backend/product_price/index.html', data)


# AddProductPrice
@login_required
def AddProductPrice(request):
    if request.method == "POST":
        form = ProductPriceForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('ProductCost')
            except:
                pass
    else:
        form = ProductPriceForm()
    return render(request, 'backend/product_price/create.html', {'form': form})


# UpdateProducePrice
@login_required
def UpdateProducePrice(request, id):
    context = {}
    obj = get_object_or_404(ProductPrice, id=id)
    form = ProductPriceForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ProductCost')
    context["form"] = form
    return render(request, 'backend/product_price/update.html', context)


#
# define the class of a form
@login_required
def Post(request):
    # check if the request is post
    if request.method == 'POST':

        # Pass the form data to the form class
        details = PostForm(request.POST)

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

            # redirect it to some another page indicating data
            # was inserted successfully
            return HttpResponse("data submitted successfully")

        else:

            # Redirect back to the same page if the data
            # was invalid
            return render(request, "backend/product/post_test.html", {'form': details})
    else:

        # If the request is a GET request then,
        # create an empty form object and
        # render it into the page
        form = PostForm(None)
        return render(request, 'backend/product/post_test.html', {'form': form})


# start look for share
@login_required
def IndexLookShareBackend(request):
    return render(request, 'backend/look_for_share/index.html')