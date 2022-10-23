from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ContactUsForm, AddressForm, AboutUsForm
from .models import AboutUs, Address


def CompanyIndex(request):
    company = AboutUs.objects.order_by('-id')
    paginator = Paginator(company, 1)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    content = {
        'company': company,
        'page': page,
    }
    return render(request, 'frontend/company/about_us/index.html', content)


def ContactUs(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('frontend')
            except:
                pass
    else:
        form = ContactUsForm()
    return render(request, 'frontend/company/contact_us/index.html', {'form': form})


def CompanyContactUs(request):
    company = AboutUs.objects.order_by('-id')

    content = {
        'company': company
    }
    return render(request, 'frontend/company/about_us/index.html', content)


def AddressView(request):
    data = Address.objects.all()

    context = {
        "data": data
    }
    return render(request, 'frontend/company/contact_us/index.html', context)


def IndexAboutUs(request):
    company = AboutUs.objects.order_by('-id')
    paginator = Paginator(company, 1)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    content = {
        'company': company,
        'page': page,
    }
    return render(request, 'backend/company/about_us/index_about.html', content)


def AddAboutUs(request):
    if request.method == "POST":
        form = AboutUsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('frontend')
            except:
                pass
    else:
        form = AboutUsForm()
    return render(request, 'backend/company/about_us/create_about.html', {'form': form})


def Contacts(request):
    data = ContactUs.objects.all()

    return HttpResponse(data)
