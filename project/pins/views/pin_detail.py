from rest_framework import generics
from ..models import Pin
from ..serializers import PinSerializer

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer