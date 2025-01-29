# subthemes/serializers.py
from rest_framework import serializers
from .models import Subtheme
from themes.serializers import ThemeSerializer
from themes.models import Theme

class SubthemeSerializer(serializers.ModelSerializer):
    theme = ThemeSerializer(read_only=True)
    theme_id = serializers.PrimaryKeyRelatedField(
        queryset=Theme.objects.all(), source='theme', write_only=True
    )

    class Meta:
        model = Subtheme
        fields = ['id', 'theme', 'theme_id', 'name', 'description', 'created_at', 'updated_at']
