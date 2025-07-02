from django.urls import path
from .views import SavePushSubscriptionView, PushSubscriptionStatusView

urlpatterns = [
    path('push/save/', SavePushSubscriptionView.as_view(), name='save_push_subscription'),
    path('push/status/', PushSubscriptionStatusView.as_view(), name='push_subscription_status'),
]
