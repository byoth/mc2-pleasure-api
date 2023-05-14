from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import permissions
from pins.models import Pin
from pins.serializers import PinSerializer
from pins.utils import get_pins

class PinList(generics.ListCreateAPIView):
    serializer_class = PinSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('category', openapi.IN_QUERY, type=openapi.TYPE_STRING, required=False, enum=['mine', 'others']),
            openapi.Parameter('center_latitude', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('center_longitude', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('latitude_delta', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('longitude_delta', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        ],
        responses={
            200: PinSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        category = self.request.query_params.get('category')
        center_latitude = self.request.query_params.get('center_latitude')
        center_longitude = self.request.query_params.get('center_longitude')
        latitude_delta = self.request.query_params.get('latitude_delta')
        longitude_delta = self.request.query_params.get('longitude_delta')

        return get_pins(self.request.user, category, center_latitude, center_longitude, latitude_delta, longitude_delta)