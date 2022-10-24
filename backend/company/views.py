from django.contrib import messages
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .forms import ContactUsForm, AddressForm, AboutUsForm, ContactUsFrontendForm
from .models import AboutUs, Address, ContactUs, ContactUsFrontend


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


# start About Us backend
# IndexAboutUs
def IndexAboutUs(request):
    company = AboutUs.objects.order_by('-id')
    paginator = Paginator(company, 2)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    content = {
        'company': company,
        'page': page,
    }
    return render(request, 'backend/company/about_us/index_about.html', content)


# function Views about us
def ViewAboutUsBackend(request, id):
    data = get_object_or_404(AboutUs, id=id)
    return render(request, 'backend/company/about_us/view_about.html', {'data': data})


# function Update about us
def UpdateAboutUsBackend(request, id):
    update_about = AboutUs.objects.get(id=id)
    if request.method == "POST":
        form = AboutUsForm(request.POST, request.FILES, instance=update_about)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successful!')
            return redirect("IndexPostBlog")
        message = 'Something we are wrong!'
        return render(request, 'backend/company/about_us/update_about.html',
                      {'message': message, 'update_about': update_about})
    else:
        form = AboutUs.objects.get(id=id)
        update_about = AboutUsForm(instance=form)
        content = {'update_about': update_about, 'id': id}
    return render(request, 'backend/company/about_us/update_about.html', content)


# Add about us backend
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


# start Contact Backend
# IndexContactBackend
def IndexContactBackend(request):
    contact_us = ContactUsFrontend.objects.order_by('-id')
    paginator = Paginator(contact_us, 12)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)

    content = {
        'contact_us': contact_us,
        'page': page,
    }
    return render(request, 'backend/company/contact_us/index_contact.html', content)


# views or detail contact us
def ViewContactUsBackend(request, id):
    data = get_object_or_404(ContactUsFrontend, id=id)
    return render(request, 'backend/company/contact_us/view_contact.html', {'data':data})


# start frontend Views
# IndexContactUsFrontend & Add Message contact us
def IndexContactUsFrontend(request):
    if request.method == "POST":
        form = ContactUsFrontendForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, 'Add Comment Successful!')
                model = form.instance
                return redirect('frontend')
            except:
                pass
    else:
        form = ContactUsFrontendForm()
    return render(request, 'frontend/company/contact_us/index.html', {'form': form})


def AddContactUsFrontend(request):
    pass

# End Frontend
