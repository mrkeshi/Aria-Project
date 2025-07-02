from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class PushSubscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='push_subscriptions')
    subscription_info = models.JSONField()
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email}"

