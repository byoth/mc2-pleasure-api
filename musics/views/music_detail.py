from rest_framework import generics
from rest_framework import permissions
from musics.models import Music
from musics.serializers import MusicSerializer

class MusicDetail(generics.RetrieveAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated,]