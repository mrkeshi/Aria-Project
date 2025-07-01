from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class OneSignalSubscription(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='onesignal')
    onesignal_user_id = models.CharField(max_length=255, unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.onesignal_user_id}"
