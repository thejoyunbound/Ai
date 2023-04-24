from django.urls import path
from .views import search

urlpatterns = [
#    path("insert/", insert),
    path("<int:year>/<int:month>/",search)
]