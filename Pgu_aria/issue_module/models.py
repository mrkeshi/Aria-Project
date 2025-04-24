from django.contrib.auth import get_user_model
from django.db import models
from django.conf import settings
from django.db.models.signals import pre_delete, m2m_changed
from django.dispatch import receiver

from workspace_module.models import *
# Create your models here.

@receiver(m2m_changed, sender=Project.users.through)
def handle_user_removal_from_project(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_remove':
        for user_id in pk_set:
            User=get_user_model()
            user = User.objects.get(id=user_id)
            Task.objects.filter(assigned=user, project=instance).delete()
            Question.objects.filter(creator=user, project=instance).delete()
            Answer.objects.filter(respondent=user,project=instance).delete()
class Question(models.Model):
  class STATUS(models.IntegerChoices):
    OPEN = '1', 'باز'
    CLOSE = '2', 'بسته'
  
  creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  subject = models.CharField(max_length=2000)
  description = models.TextField()
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, blank=True)
  status = models.PositiveSmallIntegerField(default=1, choices=STATUS)
  assigned_attached = models.FileField(upload_to='issue/question/assigned_attached', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return self.subject
  

class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
  respondent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  description = models.TextField()
  assigned_attached = models.FileField(upload_to='issue/answer/assigned_attached', null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  message_parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_answers')
  def __str__(self):
    return  self.respondent.email + self.description[:10]