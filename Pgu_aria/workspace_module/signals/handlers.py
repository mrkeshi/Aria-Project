from django.contrib.auth import get_user_model
from django.utils.timezone import now

from ..models import *
from workspace_module.models import Project
from Subcription.models import Subscription
from django.utils import timezone
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from workspace_module.models import Task
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from notification.models import PushSubscription
from pywebpush import webpush, WebPushException
import json
import logging

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

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Task)
def task_created_notification(sender, instance, created, **kwargs):
    if not created:
        return

    assigned_user = instance.assigned
    creator = instance.creator
    project = instance.project

    if not assigned_user:
        return
    duration=duration = (instance.finished_at-instance.created_at).days
    message = f"تسک با مدت زمان {duration} روز برای شما توسط {creator.get_full_name() or creator.email} در پروژه {project.title} ایجاد شد."

    try:
        subscription = PushSubscription.objects.get(user=assigned_user)
    except PushSubscription.DoesNotExist:
        logger.warning(f"No push subscription for user {assigned_user}")
        return
    user = instance.assigned
    user.current_project = instance.project
    user.save()
    print(settings.FRONTEND_BASE_URL+"/dashboard/tasks" + str(instance.id))
    payload = json.dumps({
        "title": "تسک جدید",
        "body": message,
        "icon": "/img/ali.png",
        "url": settings.FRONTEND_BASE_URL+"/dashboard/tasks/" + str(instance.id)
    })


    try:
        webpush(
            subscription_info=subscription.subscription_info,
            data=payload,
            vapid_private_key=settings.VAPID_PRIVATE_KEY,
            vapid_claims=settings.VAPID_CLAIMS
        )
        logger.info(f"Push notification sent to user {assigned_user}")
    except WebPushException as ex:
        logger.error(f"Web push failed: {repr(ex)}")

