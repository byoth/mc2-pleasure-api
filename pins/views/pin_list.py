from rest_framework import generics
from rest_framework import permissions
from pins.models import Pin
from pins.serializers import PinSerializer
from pins.utils import get_pins

class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        center_latitude = self.request.query_params.get('center_latitude')
        center_longitude = self.request.query_params.get('center_longitude')
        horizontal_radius = self.request.query_params.get('horizontal_radius')
        vertical_radius = self.request.query_params.get('vertical_radius')

        pins = get_pins(center_latitude, center_longitude, horizontal_radius, vertical_radius)

        return pins