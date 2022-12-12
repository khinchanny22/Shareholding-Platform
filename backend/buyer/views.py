from django.shortcuts import render,HttpResponse
from .forms import *

# Create your views here.


def SellersIndex(request):
    form = SellerForm()
    content = {
        'form':form
    }
    return render(request, 'backend/buyers/seller.html',content)
