from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework import permissions
from pins.models import Pin
from pin_clusters.models import PinCluster
from pin_clusters.serializers import PinClusterSerializer
from pins.utils import get_pins
from pin_clusters.utils import get_pin_clusters

class PinClusterList(generics.ListAPIView):
    serializer_class = PinClusterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('center_latitude', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('center_longitude', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('horizontal_radius', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
            openapi.Parameter('vertical_radius', openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        ],
        responses={
            200: PinClusterSerializer(many=True),
        },
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        center_latitude = self.request.query_params.get('center_latitude')
        center_longitude = self.request.query_params.get('center_longitude')
        horizontal_radius = self.request.query_params.get('horizontal_radius')
        vertical_radius = self.request.query_params.get('vertical_radius')

        pins = get_pins(center_latitude, center_longitude, horizontal_radius, vertical_radius)
        pin_clusters = get_pin_clusters(pins, 100)

        return pin_clusters