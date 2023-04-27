from django.urls import path
from musics.views import *

urlpatterns = [
    path('', MusicList.as_view()),
    path('<int:pk>', MusicDetail.as_view()),
]