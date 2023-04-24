from django.urls import path
from .views import index # views.py --> index 함수 
from .views import AppView # views.py --> AppView 클래스
from .views import http_response
from . import views
from app.views import python_data, html_page
from app.views import model_data
from app.views import redirect1, redirect2, redirect3, redirect4
from .views import text, search, search2



urlpatterns = [
    path("index/", index),
    path("index1/", AppView.as_view()),
    path("index2/,", http_response),
    path("index3/", views.template),
    path("index4/", python_data),
    path("index5/", html_page),
    path("index6/", model_data),
    path("index7/", redirect1),
    path("index8/", redirect2),
    path("index9/", redirect3),
    path("index10/", redirect4),
    path('text/<str:char>/', text),
    path('<int:year>/<int:month>/',views.date),
    path('search/', search),
    path('search/', search2),

   


]