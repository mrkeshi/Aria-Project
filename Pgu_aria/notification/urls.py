from django.urls import path
from .views import SaveOneSignalIdView, SubscriptionStatusView

urlpatterns = [
    path('save-onesignal-userid/', SaveOneSignalIdView.as_view(), name='save_onesignal_userid'),
    path('subscription/status/', SubscriptionStatusView.as_view(), name='subscription_status'),
]
