from rest_framework import viewsets

from BackAfricaOpenData.decorators import log_action
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @log_action("Created", "User")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @log_action("Updated", "User")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @log_action("Deleted", "User")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)