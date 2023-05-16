from django.db import models
from pins.models import Pin

class PinCluster():
    def __init__(self, main_pin, pin_ids, pins_count, latitude, longitude):
        self.main_pin = main_pin
        self.pin_ids = pin_ids
        self.pins_count = pins_count
        self.latitude = latitude
        self.longitude = longitude