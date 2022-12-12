from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
# documents management system index
from .forms import DmsForm
from .models import DocumentManagementSystem


@login_required
def DmsIndex(request):
    data = DocumentManagementSystem.objects.order_by('-id')
    paginator = Paginator(data, 10)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    content = {
        'data': data,
        'page': page,
    }
    return render(request, 'backend/document_management_system/index.html', content)


# function create DMS
@login_required
def CreateDmsBackend(request):
    if request.method == "POST":
        form = DmsForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('DmsIndex')
            except:
                pass
    else:
        form = DmsForm()
    return render(request, 'backend/document_management_system/create.html', {'form': form})
