from logs.models import Log
from logs.serializers import  LogSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class LogList(APIView):
    """
    List all logs, or create a new logs.
    """
    def get(self, request, format=None):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LogDetail(APIView):
    """
    Retrieve, update or delete a Log instance.
    """
    def get_object(self, pk):
        try:
            return Log.objects.get(pk=pk)
        except Log.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Log = self.get_object(pk)
        serializer = LogSerializer(Log)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Log = self.get_object(pk)
        serializer = LogSerializer(Log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Log = self.get_object(pk)
        Log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)