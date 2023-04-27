from django.urls import path
from .views import *

urlpatterns = [
    path('', PinList.as_view()),
    path('<int:pk>', PinDetail.as_view()),
]