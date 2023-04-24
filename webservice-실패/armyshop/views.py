from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Armyshop
# Create your views here.

# data = pd.read_csv('armyshop/army_shop_20210531.csv',encoding='cp949')
# data = data.to_dict('records')
# def insert(request):
#     for d in data:
#         Armyshop.objects.create(name=d['name'],year=d['year'],month=d['month'])
#     return HttpResponse('잘들어갔습니다')

def search(request,year,month):
    qr_set = Armyshop.objects.filter(year=year, month=month)
    html = '<table style="border: solid"><th>년도</th><th>월</th><th>제품명</th>'
    for c in qr_set:
        html += '<tr>'
        html += '<td>'+str(c.year)+'</td>'
        html += '<td>'+str(c.month)+'</td>'
        html += '<td>'+c.name+'</td>'
        html += '</tr>'
    html += '</table>'


    return HttpResponse(html)

def search2(request):
    year = request.GET.get("year")
    month = request.GET.get("month")
    year = int(year)
    month = int(month)
    qr_set = Armyshop.objects.filter(year=year, month=month)
    html = '<table style="border: solid"><th>년도</th><th>월</th><th>제품명</th>'
    for c in qr_set:
        html += '<tr>'
        html += '<td style="background-color:red">'+str(c.year)+'</td>'
        html += '<td>'+str(c.month)+'</td>'
        html += '<td style="color:green">'+c.name+'</td>'
        html += '</tr>'
    html += '</table>'
    return HttpResponse(html)

def get_method(request):
   
    if request.method == 'POST':
        a = request.POST.get('a')
        b = request.POST.get('b')
        c = request.POST.get('c')
        context = {
            "result":a+b+c,
            "method":'POST'
        }
    else:
        a = request.GET.get('a')
        b = request.GET.get('b')
        if a != None:
            context = {
                "result":a+b,
                "method":'GET'
               }
        else:
            context = {
                "result":'Nothing',
                "method":'undifined'
            }
    return render(request,"get.html",context)

def cat(request):
    return render(request,'cat.html')