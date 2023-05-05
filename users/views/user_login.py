from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

class UserLogin(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        token, is_token_created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})

    def handle_exception(self, exc):
        return Response({"detail": str(exc)}, status=400)