# files/serializers.py
from rest_framework import serializers
from .models import File
from subthemes.serializers import SubthemeSerializer
from subthemes.models import Subtheme

class FileSerializer(serializers.ModelSerializer):
    subtheme = SubthemeSerializer(read_only=True)
    subtheme_id = serializers.PrimaryKeyRelatedField(
        queryset=Subtheme.objects.all(), source='subtheme', write_only=True
    )

    class Meta:
        model = File
        fields = ['id', 'subtheme', 'subtheme_id', 'filename', 'file_path', 'source', 'uploaded_at', 'updated_at']
