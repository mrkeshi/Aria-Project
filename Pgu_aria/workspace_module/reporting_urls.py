from django.urls import path,include

from rest_framework_nested import routers


from  . import views as workspace_views
from . import reporting_views
app_name = 'reporting'
router  = routers.DefaultRouter()


urlpatterns = [path('ProjectDetail/<int:project_id>/',
                     reporting_views.ProjectDetail.as_view(),
                     name='project-detail'),
               path('ReportingTasksResult/',
                     reporting_views.ReportingTasksListView.as_view(),
                     name='reporting-tasks-list'),
               path('ReportingProjectProgress/',
                     reporting_views.ReportingProjectProgress.as_view(),
                     name = 'reporting-project-progress'),
               path('CompletedTaskIn10DaysAgo/',
                    reporting_views.CompletedTaskIn10DaysAgo.as_view(),
                    name = 'completed-task-in-10-days-ago'),
               path('TopUserInProject/<int:project_id>/',
                    reporting_views.TopUserInProject.as_view(),
                    name = 'top_user_in_projects'),
               path('CountOfTaskByEachTask/',
                    reporting_views.SkillTaskCountView.as_view(),
                    name='skill-task-count-view')



               ]
