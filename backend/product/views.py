from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from .models import Product


def ProductIndex(request):
    product = Product.objects.order_by('-id')
    content = {
        'product':product,
    }
    return render(request, 'backend/product/index.html', content)
