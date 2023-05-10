from pins.models import Pin

def get_pins(center_latitude, center_longitude, horizontal_radius, vertical_radius):
    if center_latitude and center_longitude and horizontal_radius and vertical_radius:
        center_latitude = float(center_latitude)
        center_longitude = float(center_longitude)
        horizontal_radius = float(horizontal_radius)
        vertical_radius = float(vertical_radius)

        min_latitude = center_latitude - horizontal_radius
        min_longitude = center_longitude - vertical_radius
        max_latitude = center_latitude + horizontal_radius
        max_longitude = center_longitude + vertical_radius
        
        return Pin.objects.filter(
            latitude__gte=min_latitude,
            latitude__lte=max_latitude,
            longitude__gte=min_longitude,
            longitude__lte=max_longitude
        )
    else:
        return Pin.objects.all()