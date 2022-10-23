from django.core.paginator import Paginator
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
    paginator = Paginator(product, 12)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'product': product,
        'page':page,
    }
    return render(request,'frontend/products/index.html',content)


def ProductDetails(request):
    return render(request,
                  'frontend/ProductDetails/index.html')


def ShoppingCart(request):
    return render(request,
                  'frontend/ShoppingCart/index.html')


def LayoutProduct(request):
    return render(request,
                  'frontend/Wishlist/index.html')
