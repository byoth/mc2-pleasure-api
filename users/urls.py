from django.urls import path
from users.views import *

urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>', UserDetail.as_view()),
    path('login', UserLogin.as_view()),
    path('signup', UserSignup.as_view()),
]