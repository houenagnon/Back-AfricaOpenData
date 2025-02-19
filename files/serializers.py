from rest_framework import serializers
from .models import File
from subthemes.serializers import SubthemeSerializer
from subthemes.models import Subtheme

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'
