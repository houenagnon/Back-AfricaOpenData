# logs/models.py
import uuid
from django.db import models
from users.models import User

class Log(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='logs')
    action = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Unknown'} - {self.action}"
    
    