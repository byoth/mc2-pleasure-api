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
            openapi.Parameter('ids', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        responses={
            200: PinSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        ids = self.request.query_params.get('ids')
        
        # TODO: remove
        category = self.request.query_params.get('category')
        center_latitude = self.request.query_params.get('center_latitude')
        center_longitude = self.request.query_params.get('center_longitude')
        latitude_delta = self.request.query_params.get('latitude_delta')
        longitude_delta = self.request.query_params.get('longitude_delta')

        if ids:
            ids_list = list(map(lambda i: int(i), ids.split(',')))
            return Pin.objects.filter(id__in=ids_list)
        else:
            return get_pins(self.request.user, category, center_latitude, center_longitude, latitude_delta, longitude_delta)