from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Login(request):
    return render(request, 'frontend/index.html')
