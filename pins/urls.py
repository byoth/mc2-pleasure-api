from django.urls import path
from pins.views import *

urlpatterns = [
    path('', PinList.as_view()),
    path('<int:pk>', PinDetail.as_view()),
    path('latest', PinLatest.as_view()),
]