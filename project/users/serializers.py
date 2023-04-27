from django.contrib.auth.models import User
from rest_framework import serializers
from pins.models import Pin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined',)