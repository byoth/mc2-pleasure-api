from django.db.models import Q
from pins.models import Pin

def get_pins(user, category=None, center_latitude=None, center_longitude=None, latitude_delta=None, longitude_delta=None):
    if category == 'mine' and user.is_authenticated:
        pins = Pin.objects.filter(user=user)
    elif category == 'others' and user.is_authenticated:
        pins = Pin.objects.filter(~Q(user=user))
    else:
        pins = Pin.objects.all()

    pins = pins.order_by('-created_at')

    if center_latitude and center_longitude and latitude_delta and longitude_delta:
        center_latitude = float(center_latitude)
        center_longitude = float(center_longitude)
        latitude_delta = float(latitude_delta)
        longitude_delta = float(longitude_delta)

        min_latitude = center_latitude - latitude_delta / 2
        min_longitude = center_longitude - longitude_delta / 2
        max_latitude = center_latitude + latitude_delta / 2
        max_longitude = center_longitude + longitude_delta / 2
        
        return pins.filter(
            latitude__gte=min_latitude,
            latitude__lte=max_latitude,
            longitude__gte=min_longitude,
            longitude__lte=max_longitude
        )
    else:
        return pins