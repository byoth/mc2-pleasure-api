from django.contrib.auth.models import User
from rest_framework import serializers
from musics.models import Music
from musics.serializers import MusicSerializer
from pins.models import Pin
from users.serializers import UserSerializer

class PinSerializer(serializers.ModelSerializer):
    music = MusicSerializer()
    user_id = serializers.IntegerField(source='user.id', read_only=True)
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Pin
        exclude = ('user',)
        read_only_fields = ('created_at',)

    def create(self, validated_data):
        music_data = validated_data.pop('music')
        music = self.__get_or_create_music(music_data)
        user = self.context['request'].user
        pin = Pin.objects.create(music=music, user=user, **validated_data)
        return pin

    def __get_or_create_music(self, music_data):
        music, created = Music.objects.get_or_create(applemusic_id=music_data['applemusic_id'])
        return music