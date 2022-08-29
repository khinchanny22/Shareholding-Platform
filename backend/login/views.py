from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Users


# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            # messages.success(request, "Logged In Successfully!!")
            return render(request, "backend/login/index.html", {"fname": fname})
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('Dashboard')

    return render(request, "backend/login/index.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('/frontend')
