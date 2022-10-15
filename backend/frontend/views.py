from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
from product.models import Product


def frontend(request):
    return render(request,
                  'frontend/index.html')


def FrontendProducts(request):
    product = Product.objects.order_by('-id')
    return HttpResponse(product)
    exit()

    content = {
        'product': product,
    }
    return render(request,
                  'frontend/products/index.html',
                  content)


def ProductDetails(request):
    return render(request,
                  'frontend/ProductDetails/index.html')


def ShoppingCart(request):
    return render(request,
                  'frontend/ShoppingCart/index.html')


def LayoutProduct(request):
    return render(request,
                  'frontend/Wishlist/index.html')
