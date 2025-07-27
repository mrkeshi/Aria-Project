from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import PushSubscription
from .serializers import PushSubscriptionSerializer


class SavePushSubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        subscription_info = request.data.get('subscription_info')

        if not subscription_info:
            return Response({"detail": "subscription_info is required."}, status=status.HTTP_400_BAD_REQUEST)

        # اگر تو subscription_info یه شناسه یکتا (مثلاً endpoint یا keys) داری،
        # اون رو برای update یا create استفاده کن:
        endpoint = subscription_info.get("endpoint")
        if not endpoint:
            return Response({"detail": "subscription_info must contain 'endpoint'."},
                            status=status.HTTP_400_BAD_REQUEST)

        obj, created = PushSubscription.objects.update_or_create(
            user=request.user,
            subscription_info__endpoint=endpoint,
            defaults={"subscription_info": subscription_info}
        )

        serializer = PushSubscriptionSerializer(obj)
        return Response({"status": "saved", "created": created, "data": serializer.data}, status=status.HTTP_200_OK)


class PushSubscriptionStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        subscriptions = request.user.push_subscriptions.all()
        serializer = PushSubscriptionSerializer(subscriptions, many=True)
        subscribed = subscriptions.exists()
        return Response({"subscribed": subscribed, "data": serializer.data})
