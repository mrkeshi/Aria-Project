from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from workspace_module.models import Project
from Subcription.models import Subscription
from django.utils import timezone
from datetime import timedelta
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
