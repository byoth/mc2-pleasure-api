from rest_framework import generics
from ..models import Pin
from ..serializers import PinSerializer

class PinList(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer