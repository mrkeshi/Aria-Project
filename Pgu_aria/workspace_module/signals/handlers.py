
from ..models import *
from workspace_module.models import Project
from Subcription.models import Subscription
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.utils import send_onesignal_notification
from notification.models import OneSignalSubscription
from workspace_module.models import Task

@receiver(post_save, sender=Project)
def create_role_for_pm(sender, created, instance, **kwargs):
  if created:
    Role.objects.create(user=instance.project_manager, project=instance)
@receiver(post_save, sender=Project)
def create_free_subscription_on_first_project(sender, instance, created, **kwargs):
    if not created:
        return

    user = instance.project_manager
    user_projects_count = Project.objects.filter(project_manager=user).count()

    if user_projects_count == 1:
        has_subscription = Subscription.objects.filter(user=user).exists()
        if not has_subscription:
            Subscription.objects.create(
                user=user,
                plan="free",
                started_at=timezone.now(),
                expires_at=timezone.now() + timedelta(days=30),
                is_active=True
            )

@receiver(post_save, sender=Task)
def send_task_assignment_notification(sender, instance, created, **kwargs):
    if created and instance.assigned:
        try:
            subscription = OneSignalSubscription.objects.get(user=instance.assigned)
            onesignal_user_id = subscription.onesignal_user_id

            heading = "تسک جدید اختصاص یافته"
            message = f"تسک '{instance.title}' در پروژه '{instance.project.title}' توسط مدیر پروژه برای شما اختصاص پیدا کرده است."

            send_onesignal_notification(onesignal_user_id, heading, message)
        except OneSignalSubscription.DoesNotExist:
            pass
        except Exception as e:
            print(f"خطا در ارسال نوتیفیکیشن تسک: {e}")
