from django.urls import path
from .views import insert, board_list, board_detail
from .views import err, sign_in, session_test

urlpatterns = [
    path("insert/", insert),
    path("list/",board_list),
    path("detail/",board_detail),
    path("err/",err),
    path("sign/",sign_in),
    path("session/",session_test)
]