from django.urls import path
from .views import search, search2, get_method,cat

urlpatterns = [
#    path("insert/", insert),
    path("<int:year>/<int:month>/",search),
    path("search/",search2),
    path("get/",get_method),
    path("cat/",cat)
]