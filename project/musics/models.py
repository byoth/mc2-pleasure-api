from django.db import models

class Music(models.Model):
    applemusic_id = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'music'