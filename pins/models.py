from django.contrib.auth.models import User
from django.db import models
from musics.models import Music

class Pin(models.Model):
    music = models.ForeignKey(Music, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    administrative_area = models.CharField(max_length=50)
    locality = models.CharField(max_length=50)
    weather = models.CharField(max_length=20)
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'pin'