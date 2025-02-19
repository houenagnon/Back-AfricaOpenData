# subthemes/serializers.py
from rest_framework import serializers
from .models import Subtheme
from themes.serializers import ThemeSerializer
from themes.models import Theme

class SubthemeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subtheme
        fields = '__all__'
