from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import permissions
from users.serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]