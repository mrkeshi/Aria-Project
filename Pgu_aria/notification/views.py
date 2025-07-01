from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import OneSignalSubscription
from .serializers import OneSignalSubscriptionSerializer

class SaveOneSignalIdView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        onesignal_user_id = request.data.get('onesignal_user_id')

        if not onesignal_user_id:
            return Response({"detail": "onesignal_user_id is required."}, status=400)

        obj, created = OneSignalSubscription.objects.update_or_create(
            user=request.user,
            defaults={"onesignal_user_id": onesignal_user_id}
        )
        return Response({"status": "saved", "created": created})


class SubscriptionStatusView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            obj = request.user.onesignal
            return Response({"subscribed": True, "onesignal_user_id": obj.onesignal_user_id})
        except OneSignalSubscription.DoesNotExist:
            return Response({"subscribed": False})
