# logs/serializers.py
from rest_framework import serializers
from .models import Log
from users.serializers import UserSerializer
from users.models import User

class LogSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )

    class Meta:
        model = Log
        fields = ['id', 'user', 'user_id', 'action', 'created_at']
