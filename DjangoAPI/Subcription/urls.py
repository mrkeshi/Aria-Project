from django.urls import path
from .views import StartPaymentAPIView, VerifyPaymentAPIView, SubscriptionStatusView

urlpatterns = [
    path('start/', StartPaymentAPIView.as_view(), name='start-payment'),
    path('verify/', VerifyPaymentAPIView.as_view(), name='verify-payment'),
    path("status/", SubscriptionStatusView.as_view(), name="subscription-status"),

]