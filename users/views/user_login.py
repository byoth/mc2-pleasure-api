from django.contrib.auth import authenticate, login
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class UserLogin(APIView):
    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('username', openapi.IN_QUERY, type=openapi.TYPE_STRING),
            openapi.Parameter('password', openapi.IN_QUERY, type=openapi.TYPE_STRING),
        ],
        responses={
            200: '{ "token": String }',
        },
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        token, is_token_created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    def handle_exception(self, exc):
        return Response({"detail": str(exc)}, status=400)