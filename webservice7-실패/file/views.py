from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.


def upload(request):
    upload_file = request.FILES.get['file']
    if upload_file != None
        name = upload_file.name
        size = upload_file.size
        context = {
            'name' = name
            'size' = size

        }
    else