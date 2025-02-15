from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from downloads.models import Download
from downloads.serializers import DownloadSerializer


class DownloadList(APIView):
    """
    List all downloads, or save a new download.
    """
    def get(self, request, format=None):
        downloads = Download.objects.all()
        serializer = DownloadSerializer(downloads, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DownloadSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save(file=request.FILES.get('file'))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DownloadDetail(APIView):
    """
    Retrieve, update or delete a Download instance.
    """
    def get_object(self, pk):
        try:
            return Download.objects.get(pk=pk)
        except Download.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        download = self.get_object(pk)
        serializer = DownloadSerializer(download)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        download = self.get_object(pk)
        serializer = DownloadSerializer(download, data=request.data, partial=True)
        if serializer.is_valid():
            if 'file' in request.FILES:
                serializer.save(file=request.FILES.get('file'))  # Mettre à jour le fichier
            else:
                serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        download = self.get_object(pk)
        download.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)