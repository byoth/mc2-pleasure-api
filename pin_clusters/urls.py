from django.urls import path
from pin_clusters.views import *

urlpatterns = [
    path('', PinClusterList.as_view()),
]