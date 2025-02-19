from BackAfricaOpenData.decorators import log_action
from themes.models import Theme
from themes.serializers import  ThemeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ThemeList(APIView):
    """
    List all themes, or create a new themes.
    """

    def get(self, request, format=None):
        themes = Theme.objects.all()
        serializer = ThemeSerializer(themes, many=True)
        return Response(serializer.data)

    @log_action("Created", "Theme")
    def post(self, request, format=None):
        serializer = ThemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ThemeDetail(APIView):
    """
    Retrieve, update or delete a Theme instance.
    """
    def get_object(self, pk):
        try:
            return Theme.objects.get(pk=pk)
        except Theme.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Theme = self.get_object(pk)
        serializer = ThemeSerializer(Theme)
        return Response(serializer.data)

    @log_action("Updated", "Theme")
    def put(self, request, pk, format=None):
        Theme = self.get_object(pk)
        serializer = ThemeSerializer(Theme, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @log_action("Deleted", "Theme")
    def delete(self, request, pk, format=None):
        Theme = self.get_object(pk)
        Theme.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)