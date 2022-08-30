from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth import get_user_model
# Create your views here.
def Dashboard(request):
    return render(request, 'backend/dashboard.html')


def User(request):
    User = get_user_model()
    users = User.objects.all()
    data = {
        'users':users
    }

    return render(request, 'backend/users/index.html', data)
