from rest_framework import serializers
from .models import PushSubscription

class PushSubscriptionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = PushSubscription
        fields = ['user', 'subscription_info', 'subscribed_at']
        read_only_fields = ['user', 'subscribed_at']