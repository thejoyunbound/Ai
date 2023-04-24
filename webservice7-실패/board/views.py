from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Board, Member
import pymysql
from sqlalchemy import create_engine, text
import pandas as pd
conn = create_engine("mysql+pymysql://root:0000@localhost:3306/webservice")

# Create your views here.

def login(request):
    if request.POST.get('user_id') == None:
        return render(request,'login.html')
    else:
        user_id = request.POST.get('user_id')
        user_pass = request.POST.get('user_pass')
        header = "select user_name from board_member "
        condition = f"where user_id='{user_id}' and user_pass='{user_pass}'" 
        stmt = header+condition
        user_name = pd.read_sql(stmt,conn).values[0][0]
        #conn.close()
        if user_name != None:
            redirect = f'/board/list/?user_name={user_name}'
            return HttpResponseRedirect(redirect)
        else:
            return render(request,'check.html')

def insert(request):
    if request.POST.get('writer') != None:
        writer = request.POST.get('writer')
        text = request.POST.get('text')
        title = request.POST.get('title')
        Board.objects.create(writer=writer, text=text, title=title, cnt=0)
        return HttpResponseRedirect("/board/list/")
    else:
        writer = request.GET.get('writer')
        context = {'writer':writer}
        return render(request,"insert.html",context)

def board_list(request):
    user_name = request.GET.get('user_name')
    condition = request.GET.get('condition')
    search = request.GET.get('search')

    if user_name == None:
        return HttpResponse('잘 못된 접근입니다')
    if condition == None:
        qr_set = Board.objects.all()
        context = {'result':qr_set,
               'user_name':user_name 
        }
        return render(request,'list.html',context)
    elif condition == 'title':
        "select * from board_board where title like '%search%'"
        qr_set = Board.objects.filter(title__contains=search)
        context = {'result':qr_set,
               'user_name':user_name 
        }
        return render(request,'list.html',context)
    elif condition == 'text':
        "select * from board_board where text like '%search%'"
        qr_set = Board.objects.filter(text__contains=search)
        context = {'result':qr_set,
                   'user_name':user_name 
        }
        return render(request,'list.html',context)

def board_detail(request):
    id = request.GET.get('id')
    user_name = request.GET.get('user_name')
    if id == None:
        return HttpResponseRedirect('../err')
    qr_set = Board.objects.filter(id=id)
    stmt =f'update board_board set cnt = cnt+1 where id = {id}'
    conn.execute(text(stmt))

    context = {
        'result':qr_set,
        'user_name':user_name
    }

    context = {
        'result':qr_set
    }
    return render(request,'detail.html',context)

def err(request):
    return render(request,'err.html')

def sign_in(request):
    user_id = request.POST.get('user_id')
    user_pass = request.POST.get('user_pass')
    user_name = request.POST.get('user_name')
    if user_id != None:
        member = Member(user_id=user_id, user_pass= user_pass, user_name=user_name)
        member.save()
        context = {
            'greeting':user_name+'님 회원가입이 완료되었습니다',
        }
    return render(request,'member.html')

def session_test(request):
    session_id = request.session.session_key
    del session_id
    session_id = request.session.session_key
    return HttpResponse(session_id)