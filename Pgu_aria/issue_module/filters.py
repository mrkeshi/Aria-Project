from django_filters.rest_framework import FilterSet
from .models import Question

class QuestionFilterSet(FilterSet):
  class Meta:
    model = Question
    fields = {
      'creator': ['exact']
    }