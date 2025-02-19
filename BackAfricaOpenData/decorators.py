from functools import wraps

from logs.models import Log
from users.models import User


def log_action(action, model):
    def decorator(func):
        @wraps(func)
        def wrapper(self, request, *args, **kwargs):
            response = func(self, request, *args, **kwargs)
            if response.status_code in [200, 201, 204]:  # Vérifie si la requête est un succès
                if request.user.is_authenticated:
                    Log.objects.create(
                        user=request.user,
                        logs_action=f"{model} {action}"
                    )
            return response

        return wrapper

    return decorator
