from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import Policy


def IndexSupportFrontend(request):
    form = SupportAdminForm()

    return render(request, 'frontend/support/index.html', {'form':form})


def IndexTermCondition(request):
    if request.method == "POST":
        form = TermConditionForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('IndexSupportFrontend')
            except:
                pass
    else:
        form = TermConditionForm()
    return render(request, 'frontend/term-condition/index.html', {'form':form})
