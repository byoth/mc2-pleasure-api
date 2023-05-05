from django.contrib.auth.models import User
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer

class UserSignup(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def handle_exception(self, exc):
        return Response({"detail": str(exc)}, status=400)