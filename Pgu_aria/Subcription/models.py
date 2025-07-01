from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
# from django.contrib.auth.models import User

class PaymentSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    authority = models.CharField(max_length=255, unique=True)
    plan = models.CharField(max_length=20)
    amount = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.plan} - {self.authority}"
class Subscription(models.Model):
    PLAN_CHOICES = (
        ("free", "رایگان"),
        ("silver", "نقره‌ای"),
        ("gold", "طلایی"),
    )

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES, default="free")
    started_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    transaction_id = models.CharField(max_length=255, null=True, blank=True)

    def add_days(self, days: int):
        now = timezone.now()
        if self.expires_at and self.expires_at > now:
            self.expires_at += timedelta(days=days)
        else:
            self.expires_at = now + timedelta(days=days)
        self.is_active = True
        self.save()

    def activate_plan(self, new_plan, new_plan_days, new_plan_price, transaction_id=None):
        now = timezone.now()

        if self.expires_at and self.expires_at > now:
            remaining_days = (self.expires_at - now).days
        else:
            remaining_days = 0

        old_price = {
            "free": 0,
            "silver": 990000,
            "gold": 190000,
        }.get(self.plan, 0)

        price_ratio = old_price / new_plan_price if new_plan_price > 0 else 0
        transferable_days = int(remaining_days * price_ratio)

        if self.plan == new_plan and self.expires_at and self.expires_at > now:
            self.expires_at += timedelta(days=new_plan_days)
        else:
            self.expires_at = now + timedelta(days=new_plan_days + transferable_days)

        if self.started_at is None:
            self.started_at = now

        self.plan = new_plan
        self.is_active = True
        self.transaction_id = transaction_id
        self.save()


