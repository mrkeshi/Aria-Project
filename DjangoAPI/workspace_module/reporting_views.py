from datetime import timedelta

from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.db.models import Avg, Count, Q
from django.db.models.functions import TruncDate
from django.utils import timezone
from django.db.models import Count
from .models import Task, Role

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView,RetrieveAPIView
from rest_framework.response import Response
from workspace_module.models import Project, Task, Role
from workspace_module.serializers import ReportingTaskSerializer, SkillTaskCountViewSerializer

from .serializers import CompletedTaskIn10DaysAgoSerializer,Top4UserInProjectSerializer
from issue_module.models import Question
User = get_user_model()


class ProjectDetail(APIView):
    def get(self,request,project_id):
        try:
            user = self.request.user
            project = get_object_or_404(Project,id = project_id)
        except:
            return Response({"detail": "project id is invalid or user not signed up "}, status=status.HTTP_204_NO_CONTENT)
        developers_of_project = project.users.all().count()
        print(developers_of_project)
        project_task_count = project.tasks.count()
        print(project_task_count)
        user_projects_count = Project.objects.filter(project_manager=user).count() + Project.objects.filter(
            Q(users=user) & ~Q(project_manager=user)
        ).count()

        questions = Question.objects.filter(task__project=project,status=1).count()
        print(user_projects_count)
        print('questions:',questions)
        if False:
            return Response({"detail": "No data available"}, status=status.HTTP_204_NO_CONTENT)
        return Response({ 'developers_of_project': developers_of_project,
                              'project_task_count': project_task_count,
                              'user_projects': user_projects_count,
                              'questions':questions},
                                status=status.HTTP_200_OK)
class ReportingTasksListView(ListAPIView):
    serializer_class = ReportingTaskSerializer
    def get_queryset(self):
        user = self.request.user
        try:
            tasks = user.current_project.tasks
            return tasks
        except AttributeError :
            return {'status':status.HTTP_204_NO_CONTENT}
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if status.HTTP_204_NO_CONTENT in queryset.values():
            return Response({'detail':'no project assocaited with user'}, status=status.HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
class ReportingProjectProgress(APIView):
    def get_queryset(self):
        user = self.request.user
        try:
            project = user.current_project
            tasks_total_rate = project.tasks.aggregate(Project_Progress=Avg('rate'))
            return tasks_total_rate
        except AttributeError :
            return {'status':status.HTTP_204_NO_CONTENT}
    def get(self,request):
        queryset = self.get_queryset()
        if status.HTTP_204_NO_CONTENT in queryset.values():
            return Response({'detail':'no project associated with user'}, status=status.HTTP_204_NO_CONTENT)
        return Response(queryset,status=status.HTTP_200_OK)



class CompletedTaskIn10DaysAgo(ListAPIView):
    serializer_class = CompletedTaskIn10DaysAgoSerializer

    def get_queryset(self):
        user = self.request.user
        try:
            project = user.current_project
            today = timezone.now().date()
            start_date = today - timedelta(days=9)
            all_dates = {start_date + timedelta(days=i): 0 for i in range(10)}
            completed_tasks = project.tasks.filter(
                done=True,
                updated_at__date__gte=start_date,
                updated_at__date__lte=today
            ).annotate(date=TruncDate('updated_at')) \
             .values('date') \
             .annotate(count=Count('id')) \
             .order_by('date')

            for task in completed_tasks:
                task_date = task['date']
                if task_date in all_dates:
                    all_dates[task_date] = task['count']

            result = [{'date': date, 'count': count} for date, count in all_dates.items()]
            return result

        except AttributeError:
            return None

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset is None:
            return Response({'detail': 'No project associated with user'}, status=status.HTTP_204_NO_CONTENT)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



class TopUserInProject(ListAPIView):
    serializer_class = Top4UserInProjectSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['project_id'] = self.kwargs.get('project_id')
        return context

    def get_queryset(self):
        project_id = self.kwargs.get('project_id')

        top_users = User.objects.filter(
            users=project_id
        ).annotate(
            completed_task_count=Count('task_creator', filter=Q(task_creator=True)),
            average_score=Avg('task_creator__rate')
        ).order_by('-average_score')[:4]

        print(top_users)
        return top_users
class SkillTaskCountView(APIView):
    def get(self, request,):
        if self.request.user.current_project is None:
            return Response({'detail':'no project associated with user'},status=status.HTTP_404_NOT_FOUND)
        task_counts = (
            Task.objects.filter(project=self.request.user.current_project)
            .select_related('assigned')
            .prefetch_related('assigned__role__skill')
            .values('assigned__username', 'assigned__role__skill__name')
            .annotate(task_count=Count('id'))
            .order_by('assigned__username', 'assigned__role__skill__name')
            )
        serializer_data = SkillTaskCountViewSerializer(task_counts,many=True).data
        return Response(serializer_data,status=status.HTTP_200_OK)


