from rest_framework import generics
from pins.models import Pin
from pins.serializers import PinSerializer
from shared.permissions import IsOwnerOrReadOnly

class PinDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pin.objects.all()
    serializer_class = PinSerializer
    permission_classes = [IsOwnerOrReadOnly,]