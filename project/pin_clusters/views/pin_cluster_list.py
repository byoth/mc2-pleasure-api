from rest_framework import generics
from rest_framework import permissions
from pins.models import Pin
from pin_clusters.models import PinCluster
from pin_clusters.serializers import PinClusterSerializer
from pin_clusters.utils import get_pin_clusters

class PinClusterList(generics.ListAPIView):
    serializer_class = PinClusterSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        pins = Pin.objects.all()
        radius = float(self.request.query_params.get('radius', 0))
        pin_clusters = get_pin_clusters(pins, radius)
        return pin_clusters