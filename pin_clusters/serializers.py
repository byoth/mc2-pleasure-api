from rest_framework import serializers
from pins.models import Pin
from pins.serializers import PinSerializer
from pin_clusters.models import PinCluster

class PinClusterSerializer(serializers.Serializer):
    main_pin = PinSerializer(read_only=True)
    pin_ids = serializers.ListField(child=serializers.IntegerField())
    pins_count = serializers.IntegerField()
    latitude = serializers.DecimalField(max_digits=9, decimal_places=6)
    longitude = serializers.DecimalField(max_digits=9, decimal_places=6)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['latitude'] = float(ret['latitude'])
        ret['longitude'] = float(ret['longitude'])
        return ret