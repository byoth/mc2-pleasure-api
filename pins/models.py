from django.contrib.auth.models import User
from django.db import models
from musics.models import Music

class Pin(models.Model):
    WEATHER_CHOICES = (
        ('sunny', 'Sunny'),
        ('cloudy', 'Cloudy'),
        ('rainy', 'Rainy'),
        ('snowy', 'Snowy'),
    )

    music = models.ForeignKey(Music, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    location_name = models.CharField(max_length=100, null=True)
    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES, null=True)
    temperature = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pin'