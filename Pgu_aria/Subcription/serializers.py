from rest_framework import serializers
from django.utils import timezone

from Subcription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    days_left = serializers.SerializerMethodField()

    class Meta:
        model = Subscription
        fields = ['plan', 'started_at', 'expires_at', 'is_active', 'transaction_id', 'days_left']

    def get_days_left(self, obj):
        if obj.expires_at:
            delta = obj.expires_at - timezone.now()
            return max(delta.days, 0)
        return 0
class SubscriptionStatusSerializer(serializers.Serializer):
    plan = serializers.CharField()
    started_at = serializers.DateTimeField()
    expires_at = serializers.DateTimeField(allow_null=True)
    is_active = serializers.BooleanField()
    remaining_days = serializers.IntegerField()
    total_projects = serializers.IntegerField()
    total_tasks = serializers.IntegerField()
    total_users = serializers.IntegerField()
    limits = serializers.DictField()
    manager_plan=serializers.CharField()
    manager_plan_active=serializers.BooleanField()