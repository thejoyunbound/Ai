from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.forms.models import model_to_dict
from .models import Biz

# Create your views here.
class AppView(generic.ListView):
    template_name = 'app/index1.html'
    context_object_name = 'name'
    def get_queryset(self):
        return Biz.objects.all()

def index(request):
    qr_set = Biz.objects.all()
    context={'result':qr_set}
    return render(request,'app/index.html',context)

def http_response(request):
    ## text/html
    return HttpResponse('<a href="http://naver.com">네이버</a>')

def template(request):
    data = {
        'str':'text',
        'num':10,
        'list':[1,2,3],
        'dict':{'a':'aaa','b':'bbb'},
    }
    return render(request,'template.html',context=data)

def python_data(request):
    data = {'key1':'value1','key2':'value2'}
    return JsonResponse(data)

def html_page(requet):
    return HttpResponse("<html><body>{'key1':'value1','key2':'value2'}</body><html>")

def model_data(request):
    qr_set = Biz.objects.all()
    data = []
    for c in qr_set:
        c = model_to_dict(c)
        data.append(c)
    return JsonResponse(data, safe=False)

def redirect1(request):
    return HttpResponseRedirect('../../main')

def redirect2(request):
    return HttpResponseRedirect('../index2')

def redirect3(request):
    return HttpResponseRedirect('/app/index2')

def redirect4(request):
    return HttpResponseRedirect('https://daum.net')

def redirect5(request):
    url = "http://localhost:8000/app/index2"
    return HttpResponseRedirect(url)

def text(request, char):
    char = 'ddddd '+char
    return HttpResponse(char)

def date(request,year,month):
    result = f'오늘날짜는 {year}년 {month}월 입니다'
    return HttpResponse(result)

def search(request):
    title = request.GET.get("name")
    return HttpResponse(f'검색어는 {title} 입니다')

def search2(request):
    title = request.GET.get('title')
    actor = request.GET.get('actor')
    html = '<html> 찾은 영화제목은 <body> <p style="color:red"> '
    html += title
    html += '</p> 배우는 <p style="color:blue">'
    html += actor
    html += '</p> </html>'
    return HttpResponse(html)