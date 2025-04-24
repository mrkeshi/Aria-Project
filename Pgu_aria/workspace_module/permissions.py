from rest_framework import permissions
from .models import Role, Project


class PermissionPM(permissions.BasePermission):
  def has_permission(self, request, view):
    project_id =request.user.current_project.id

    if request.user.is_authenticated:
      return Project.objects.filter(pk=project_id).exists()
    return False

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



