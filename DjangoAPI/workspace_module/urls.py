from os.path import basename

from django.urls import path,include

from rest_framework_nested import routers

from issue_module.views import *
from  . import views as workspace_views
app_name = 'workspace_module'
router  = routers.DefaultRouter()


router.register(r'project',workspace_views.ProjectViewSet,basename='project')
router.register(r'task',workspace_views.TaskViewSet,basename='task')
router.register(r'createTaskCategory',workspace_views.CreateTaskCategory,basename='create_task_category')
router.register(r'updateTaskCategory',workspace_views.UpdateCategoryToTaskViewSet,basename='update_task_categories')
router.register(r'get-user-level',workspace_views.GetUserLevel,basename='get_user_level')
router.register(r'create-skill',workspace_views.CreateSkill,basename='Create_skill')

router2 = routers.NestedSimpleRouter(router, 'project', lookup='project')
router2.register('role',workspace_views.RoleViewSet, basename='project-role')
router2.register('questions',IssueViewSet,basename='project-questions')
question_router = routers.NestedSimpleRouter(router2, 'questions', lookup='question')
question_router.register('answers', AnswerViewSet, basename='questions-answers')


urlpatterns = router.urls + router2.urls + question_router.urls
urlpatterns = urlpatterns + [path('project/<int:project_pk>/email/', workspace_views.InviteUserViewSet.as_view({'get': 'retrieve', 'post': 'create'}), name='invite_user'),
                             path('project/<int:project_pk>/email/<str:email>', workspace_views.AcceptInviteUserViewSet.as_view(), name='accept_invite_user'),
                             path('project/<int:project_pk>/get_user_level_skill', workspace_views.GetLevelSkillView.as_view(), name='get_level_skill'),
                             path('project/<int:project_pk>/users/', workspace_views.ListUserViewSet.as_view({'get':'list'}), name='project-user'),
                             path('project/<int:project_pk>/users/<int:user_id>', workspace_views.DeleteUserProjectViewSets.as_view({'post':'delete'}), name='project-user'),
                             ]



