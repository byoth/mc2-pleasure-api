from rest_framework import serializers
from .models import Pin
from musics.models import Music
from musics.serializers import MusicSerializer

class PinSerializer(serializers.ModelSerializer):
    music = MusicSerializer()

    class Meta:
        model = Pin
        fields = '__all__'
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        music_data = validated_data.pop('music')
        music = self.__get_or_create_music(music_data)
        pin = Pin.objects.create(music=music, **validated_data)
        return pin

    def __get_or_create_music(self, music_data):
        music, created = Music.objects.get_or_create(applemusic_id=music_data['applemusic_id'])
        return music