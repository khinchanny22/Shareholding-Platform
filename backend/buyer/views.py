from django.shortcuts import render


# Create your views here.
def SellersIndex(request):
    return render(request, 'backend/buyers/seller.html')
