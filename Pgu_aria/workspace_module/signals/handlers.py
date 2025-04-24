from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import *

@receiver(post_save, sender=Project)
def create_role_for_pm(sender, created, instance, **kwargs):
  if created:
    Role.objects.create(user=instance.project_manager, project=instance)