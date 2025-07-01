from rest_framework import serializers
from .models import OneSignalSubscription

class OneSignalSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneSignalSubscription
        fields = ['onesignal_user_id']