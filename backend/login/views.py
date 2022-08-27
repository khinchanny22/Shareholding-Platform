from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def Login(request):
    return render(request, 'backend/dashboard.html')


def Backend(request):
    pass
