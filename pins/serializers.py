from rest_framework import serializers
from musics.models import Music
from musics.serializers import MusicSerializer
from pins.models import Pin

class PinSerializer(serializers.ModelSerializer):
    music = MusicSerializer()

    class Meta:
        model = Pin
        exclude = ('user',)
        read_only_fields = ('created_at',)

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['latitude'] = float(ret['latitude'])
        ret['longitude'] = float(ret['longitude'])
        return ret

    def create(self, validated_data):
        music_data = validated_data.pop('music')
        music = self.__update_or_create_music(music_data)
        user = self.context['request'].user
        pin = Pin.objects.create(music=music, user=user, **validated_data)
        return pin

    def __update_or_create_music(self, music_data):
        music, created = Music.objects.update_or_create(
            applemusic_id=music_data['applemusic_id'],
            defaults=music_data
        )
        return music