from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from pins.models import Pin
from pins.serializers import PinSerializer
from pins.utils import get_pins

class PinLatest(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        category = self.request.query_params.get('category')
        pins = get_pins(self.request.user, category)
        pin = pins.latest('created_at')
        serializer = PinSerializer(pin)
        return Response(serializer.data)