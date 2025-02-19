from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from themes.models import Theme
from .models import Subtheme
from .serializers import SubthemeSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class SubthemeListCreateAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, theme_id, *args, **kwargs):
        """Lister les sous-thèmes d'une thématique spécifique"""
        try:
            theme = Theme.objects.get(id=theme_id)
            subthemes = Subtheme.objects.filter(theme_id=theme.id)
            serializer = SubthemeSerializer(subthemes, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Theme.DoesNotExist:
            return Response({"error": "Thématique non trouvée."}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        """Créer un nouveau sous-thème pour une thématique
        if not request.user.is_admin:
            return Response({"error": "Permission refusée."}, status=status.HTTP_403_FORBIDDEN)"""
        
        try:
            # Vérifie que le thème existe
            if Theme.objects.get(id=theme_id):
                data = request.data.copy()  # Crée une copie mutable de request.data
            serializer = SubthemeSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Theme.DoesNotExist:
            return Response({"error": "Thématique non trouvée."}, status=status.HTTP_404_NOT_FOUND)

class SubthemeDetailAPIView(APIView):
    #permission_classes = [IsAuthenticated]

    def get(self, request, id, *args, **kwargs):
        """Détails d'un sous-thème spécifique"""
        try:
            subtheme = Subtheme.objects.get(id=id)
            serializer = SubthemeSerializer(subtheme)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Subtheme.DoesNotExist:
            return Response({"error": "Sous-thème non trouvé."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id, *args, **kwargs):
        """Mettre à jour un sous-thème existant
        if not request.user.is_admin:
            return Response({"error": "Permission refusée."}, status=status.HTTP_403_FORBIDDEN)"""
        
        try:
            subtheme = Subtheme.objects.get(id=id)
            serializer = SubthemeSerializer(subtheme, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Subtheme.DoesNotExist:
            return Response({"error": "Sous-thème non trouvé."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, *args, **kwargs):
        """Supprimer un sous-thème
        if not request.user.is_admin:
            return Response({"error": "Permission refusée."}, status=status.HTTP_403_FORBIDDEN)"""
        
        try:
            subtheme = Subtheme.objects.get(id=id)
            subtheme.delete()
            return Response({"message": "Sous-thème supprimé avec succès."}, status=status.HTTP_204_NO_CONTENT)
        except Subtheme.DoesNotExist:
            return Response({"error": "Sous-thème non trouvé."}, status=status.HTTP_404_NOT_FOUND)
