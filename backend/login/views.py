from django.http import HttpResponse, request
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Users


# Create your views here.


def Login(request):
    if request.method == "GET":
        return render(request, 'login/index.html')
    username = request.POST.get('user')
    password = request.POST.get('pwd')

    user = Users.objects.get(id=1)
    user_name = user.username
    pass_word = user.password

    if username == user_name and password == pass_word:
        return HttpResponse('Hello')
    return render(request, "login/index.html", {'error_msg': 'hello'})


def Backend(request):
    pass
