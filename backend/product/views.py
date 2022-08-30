from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ProductForm, ProductPriceForm
from .models import *


def ProductIndex(request):
    product = Product.objects.order_by('-id')
    content = {
        'product': product,
    }
    return render(request, 'backend/product/index.html', content)


def ProductCost(request):
    product = ProductPrice.objects.order_by('-id')
    data = {
        'product': product,
    }
    return render(request, 'backend/product_price/index.html', data)


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


def AddProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('ProductIndex')
            except:
                pass
    else:
        form = ProductForm()
    return render(request, 'backend/product/create.html', {'form': form})


def UpdateProduct(request, id):
    context = {}

    obj = get_object_or_404(Product, id=id)

    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('ProductIndex')

    context["form"] = form
    return render(request, 'backend/product/update.html', context)
