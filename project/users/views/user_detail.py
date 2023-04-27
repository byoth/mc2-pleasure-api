from django.contrib.auth.models import User
from rest_framework import generics
from shared.permissions import IsMeOrReadOnly
from users.serializers import UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsMeOrReadOnly,]