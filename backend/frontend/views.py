from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def frontend(request):
    return render(request, 'frontend/index.html')
