from . import views as workspace_views
from .urls import router2
from django.urls import path
from rest_framework_nested import routers

app_name = 'Manager_task'
router = routers.DefaultRouter()

router.register(r'ManagerManageTasks',workspace_views.ProjectOwnerManageTaskViewSet,basename='ManagerManageTasks')
router.register(r'UserTasks', workspace_views.UserManageTaskViewSet, basename='TaskDetails')
router.register(r'ManageTasks',workspace_views.MangeTaskBySeniorOrManager,basename='ManageTasks')

urlpatterns = router.urls
urlpatterns+= [
    path('users-with-skill/<int:skill_id>', workspace_views.GetUsersWithSkillView.as_view(), name='users-with-skill'),
]