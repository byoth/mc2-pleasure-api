from django.contrib.auth.models import User
from django.db import IntegrityError
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from users.serializers import UserSerializer

class UserSignup(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        responses={
            200: UserSerializer(),
        },
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.create_user(username=username, password=password)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def handle_exception(self, exc):
        return Response({"detail": str(exc)}, status=400)