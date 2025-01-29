# downloads/models.py
import uuid
from django.db import models
from users.models import User
from files.models import File

class Download(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='downloads')
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='downloads')
    
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} downloaded {self.file.filename}"
