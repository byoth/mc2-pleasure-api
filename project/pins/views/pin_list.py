from rest_framework import generics
from rest_framework import permissions
from pins.models import Pin
from pins.serializers import PinSerializer

class PinList(generics.ListCreateAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]