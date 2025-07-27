from rest_framework import permissions
from rest_framework.response import Response

from issue_module.models import Question, Answer
from workspace_module.models import Role, Project
from rest_framework import status

class PermissionUserProject(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.user.current_project:
      project_id =request.user.current_project.id
      return Project.objects.filter(project_id=project_id).exists()
    return False
      

class PermissionPM(permissions.BasePermission):
  def has_permission(self, request, view):
    try:
      project_id =request.user.current_project.id
      project = Project.objects.get(pk=project_id)
      return request.user == project.project_manager
    except Project.DoesNotExist:
      return Response({'message' : 'این پروژه وجود نذارد'}, status=status.HTTP_400_BAD_REQUEST)
    except AttributeError:
      return Response({'message': 'شما در حال حاضر پروژه در جریان خود را تعیین نکردید'}, status=status.HTTP_400_BAD_REQUEST)

class IsProjectManagerOrSenior(permissions.BasePermission):

    def has_object_permission(self, request, view,obj):
        if request.user == obj.project.project_manager:
          return True
        elif request.user == obj.creator:
          return True
        return False

class IsProjectOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.project.project_manager
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
class IsPutPatchOrGet(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in ['PUT', 'PATCH', 'GET']
      
class IsUserInProject(permissions.BasePermission):
  
  def has_permission(self, request, view):
    project_id = view.kwargs.get('project_id')
    try:
      project = Project.objects.get(id=project_id)
      return (request.user in project.users.all() or request.user == project.project_manager)
    except Project.DoesNotExist:
      return Response({'message': 'پروژه مورد نظر وجود ندارد'}, status=status.HTTP_400_BAD_REQUEST)

class CreatorQuestionProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        question_id = view.kwargs.get('pk')

        try:
            question = Question.objects.get(id=question_id)
            print("hhhhhhhhhhhhhh")
            print(request.user)
            print(question.creator)
            return (question.creator == request.user or request.user.current_project.project_manager==request.user)
        except Question.DoesNotExist:
            return False


class CreatorAnswerProjectPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        answer_id = view.kwargs.get('pk')
        try:
            answer = Answer.objects.get(pk=answer_id)
            return (answer.respondent == request.user)
        except Answer.DoesNotExist:
            return False