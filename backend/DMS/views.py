from django.shortcuts import render


# Create your views here.
# documents management system index
def DmsIndex(request):
    return render(request, 'backend/document_management_system/index.html')
