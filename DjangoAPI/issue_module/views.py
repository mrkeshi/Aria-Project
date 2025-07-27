
from django.db.models import Max, F, Case, When,Value
from django.db.models.functions import Coalesce, Least
from django.shortcuts import render
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import ModelViewSet

from Subcription.models import Subscription
from issue_module.models import Question, Answer
from issue_module.serializers import QuestionSerializer, SimpleAnswerSerializer
from utils.permissions import IsUserInProject, PermissionPM, CreatorQuestionProjectPermission, \
  CreatorAnswerProjectPermission

from django_filters.rest_framework import DjangoFilterBackend

from workspace_module.models import Project
from .filters import QuestionFilterSet

# Create your views

class IssueViewSet(ModelViewSet):
  serializer_class = QuestionSerializer
  filter_backends = (DjangoFilterBackend,)
  filterset_class = QuestionFilterSet
  def get_queryset(self, *args, **kwargs):
    project = Project.objects.filter(id=self.request.user.current_project.id).first()
    manager = project.project_manager
    sub = Subscription.objects.get(user=manager)
    try:

      is_invalid = (sub.plan == "free") or (not sub.is_active)
      if is_invalid:
        raise PermissionDenied("اشتراک مدیر پروژه معتبر نیست.")
    except Subscription.DoesNotExist:
      raise PermissionDenied("مدیر پروژه هیچ اشتراکی ندارد.")

    project_id = self.kwargs.get('project_pk')
    questions = Question.objects.prefetch_related('answers').annotate(
      last_answer_date=Max('answers__updated_at')
    ).annotate(
      sort_date=Case(
        When(last_answer_date__lt=F('updated_at'), then=F('updated_at')),
        default=Coalesce('last_answer_date', F('updated_at'))
      )
    ).filter(project=project_id).order_by('-sort_date')


    return questions

  def get_permissions(self):
    if self.action in ['destroy']:
      # PermissionPM(),
      return [ CreatorQuestionProjectPermission()]
    elif self.action in ['update', 'partial_update']:
      return [CreatorQuestionProjectPermission()]
    else:
      return [IsUserInProject()]

class AnswerViewSet(ModelViewSet):
  serializer_class = SimpleAnswerSerializer
  permission_classes = [IsUserInProject]

  def get_queryset(self, *args, **kwargs):
    print("ddddddddaaaaaaaaaaaaaaaaaaaaaadddddd")
    question_id = self.kwargs.get('question_pk')
    return Answer.objects.prefetch_related('sub_answers').filter(question=question_id)

  def get_permissions(self):
    if self.action in ['destroy']:

      return [PermissionPM(), CreatorAnswerProjectPermission()]
    elif self.action in ['update', 'partial_update']:
      return [CreatorAnswerProjectPermission()]
    else:
      return [IsUserInProject()]