# downloads/serializers.py
from rest_framework import serializers
from .models import Download
from users.serializers import UserSerializer
from users.models import User
from files.serializers import FileSerializer
from files.models import File

class DownloadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source='user', write_only=True
    )
    file = FileSerializer(read_only=True)
    file_id = serializers.PrimaryKeyRelatedField(
        queryset=File.objects.all(), source='file', write_only=True
    )

    class Meta:
        model = Download
        fields = ['id', 'user', 'user_id', 'file', 'file_id', 'downloaded_at']
