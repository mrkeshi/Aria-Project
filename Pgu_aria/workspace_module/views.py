import pytz
from django.contrib.auth.hashers import make_password
from django.db.models import Q, When,Case
from django.shortcuts import get_object_or_404
from django.core.validators import validate_email
from rest_framework import generics
from .emails import send_invitation_email
from rest_framework import exceptions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import status
from rest_framework.exceptions import ValidationError as RestFrameWorkValidationError
from utils.permissions import  PermissionPM , IsPutPatchOrGet,IsProjectManagerOrSenior
from .serializers import *
from core.serializers import CustomUserSerializer
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilterSet

# User = get_user_model()
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes= [IsAuthenticated]

    # def get_serializer_class(self):
    #     if self.request.method == "GET":
    #         return ListProjectSerializer
    #     return ProjectSerializer
    def get_queryset(self, *args):
        user = self.request.user
        if user is not None:

            return Project.objects.filter(project_manager=user.id)
    
    def perform_create(self, serializer):
        project=serializer.save(project_manager=self.request.user)
        if(self.request.user.current_project):
            pass
        else:
            self.request.user.current_project=project
            self.request.user.save()

    def list(self, request, *args, **kwargs):
        item_id = request.query_params.get('id', None)
        queryset = self.get_queryset(item_id)

        if not queryset:
            return Response({"message": "No projects found."}, status=404)

        projects_data = []
        seen_ids = set()

        for project in queryset:
            if project.id not in seen_ids:
                tasks = Task.objects.filter(project_id=project.id)
                sum_rate = 0
                average_rate = 0
                for task in tasks:
                    if task.progress is None:
                        continue
                    else:
                        sum_rate += task.progress

                        if tasks.count()==0:
                            average_rate=100
                        else:
                            average_rate = sum_rate/tasks.count()


                project_data = {
                    'id': project.id,
                    'title': project.title,
                    'user_count': project.users.count(),
                    'description': project.description,
                    'status': project.status,
                    'Progress': average_rate%100,
                    'project_admin': CustomUserSerializer(project.project_manager).data
                }
                projects_data.append(project_data)
                seen_ids.add(project.id)

        return Response(projects_data)
    def retrieve(self, request, *args, **kwargs):
        project_id = kwargs.get('pk')

        try:
            project = Project.objects.get(pk=project_id)

            if request.user == project.project_manager or request.user.current_project==project:

                serializer = self.get_serializer(project)
                return Response(serializer.data)
            else:
                return Response({"detail": "شما به این پروژه دسترسی ندارید."}, status=403)
        except Project.DoesNotExist:
            return Response({"detail": "پروژه یافت نشد."}, status=404)

    def get_queryset(self, *args):
        user = self.request.user
        if user is not None:
            if user.current_project is not None:
                queryset = Project.objects.filter(
                    Q(project_manager=user) | Q(users=user)
                ).annotate(
                    is_current=Case(
                        When(id=user.current_project.id, then=1),
                        default=0,
                    )
                ).order_by('-is_current')
            else:
                queryset = Project.objects.filter(
                    Q(project_manager=user) | Q(users=user)
                )

            return queryset

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance =request.user.current_project

        if instance.project_manager != request.user:
            return Response({"detail": "شما مجاز به ویرایش این پروژه نیستید."}, status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'], url_path='set-current-project')
    def set_current_project(self, request):

        print(request.query_params)
        project_id = request.query_params.get('project_id', None)
        if project_id is None:
            return Response({"detail": "project_id parameter is required."}, status=400)
        project = get_object_or_404(Project, id=project_id)
        if project.project_manager != request.user and request.user not in project.users.all():
            return Response({"detail": "You do not have permission to set this project as current."}, status=403)
        print(self.request.user)
        current_user = get_object_or_404(User, id=self.request.user.id)
        print('current project',current_user.current_project)
    # Set the current project for the user
        current_user.current_project = project
        current_user.save()
        print('current project',current_user.current_project)
        serializer = self.get_serializer(project)
        print('serializer',serializer)
        print(serializer.data)
        return Response(serializer.data)

    @action(detail=False,methods=['get'],url_path='user-level')
    def get_current_user_level_project(self,request):
        user_id = request.query_params.get('user-id', None)
        if user_id is None:
            return Response({"detail": "user_id parameter is required."}, status=400)

        user = get_object_or_404(User, id=user_id)
        serializer = ProjectSerializer(user.current_project)
        return Response(serializer.data)
    @action(detail=False, methods=['get'], url_path='user-level')
    def get_current_user_level_project(self, request):
        user_id = request.query_params.get('user-id', None)
        if user_id is None:
            return Response({"detail": "user_id parameter is required."}, status=400)

        user = get_object_or_404(User, id=user_id)
        serializer = ProjectSerializer(user.current_project)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):

        project = self.get_object()
        if project.project_manager == request.user:
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:

            if request.user in project.users.all():
                project.users.remove(request.user)
                return Response({"detail": "شما از پروژه حذف شدید."}, status=status.HTTP_200_OK)

            return Response({"detail": "شما مجاز به حذف این پروژه نیستید."}, status=status.HTTP_403_FORBIDDEN)






class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet

# مدیر  یا سنیور می تواند تسک تعریف کند.
# قسمت مهم مدیریت تسک ها
class ProjectOwnerManageTaskViewSet(viewsets.ModelViewSet):
    """project manger can change anything in tasks """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated,IsProjectManagerOrSenior]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet
    def perform_create(self, serializer):
        print("Hi")
        task_instance = serializer.save(creator=self.request.user,project = self.request.user.current_project)
        if task_instance.finished_at and task_instance.finished_at < task_instance.created_at:
            task_instance.delete()
            raise RestFrameWorkValidationError("Finished date cannot be earlier than created date.")


    def get_queryset(self,*args,**kwargs):
        project = self.request.user.current_project
        tasks = Task.objects.filter(project=project)
        return tasks

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        finished_at_str = request.data.get('finished_at', None)
        if finished_at_str:
            try:
               finished_at = datetime.strptime(finished_at_str, "%Y-%m-%d %H:%M:%S")  # Adjust format as needed
            except ValueError:
                raise RestFrameWorkValidationError("Invalid date format for finished_at. Use YYYY-MM-DD.")
            if finished_at < task.created_at:
                raise RestFrameWorkValidationError("Finished date cannot be earlier than created date.")
        return super(ProjectOwnerManageTaskViewSet, self).update(request, *args, **kwargs)

    def get_serializer_class(self):
        """
        Returns a different serializer class for update action.
        """
        if self.action == 'update':
            return TaskUpdateSerializer  # سریالایزر مخصوص آپدیت
        if self.action == "list":
            return TaskSerializerRead
        return super().get_serializer_class()

class MangeTaskBySeniorOrManager(viewsets.ModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet
    """senior  creator of task or project manager have full access to change task """
    serializer_class = TaskSeniorUserSerializer
    permission_classes = [IsProjectManagerOrSenior,IsAuthenticated]
    def perform_create(self, serializer):


        task_instance =serializer.save(creator=self.request.user.id,project=self.request.user.current_project)
        if task_instance.finished_at and task_instance.finished_at < task_instance.created_at:
            task_instance.delete()
            raise RestFrameWorkValidationError("Finished date cannot be earlier than created date.")

    def get_queryset(self):

        user = self.request.user
        project = user.current_project
        if project.project_manager == user:
            return Task.objects.filter(project_id=project.id)
        return Task.objects.filter(project_id=project.id, creator=user) | Task.objects.filter(project_id=project.id, assigned=user)

    def update(self, request, *args, **kwargs):

        task = self.get_object()
        finished_at_str = request.data.get('finished_at', None)
        if finished_at_str:
            try:



                finished_at = datetime.strptime(finished_at_str,"%Y-%m-%d %H:%M:%S")
                finished_at=pytz.UTC.localize(finished_at)


               # Adjust format as needed
            except ValueError:
                raise RestFrameWorkValidationError("Invalid date format for finished_at. Use YYYY-MM-DD.")
            if finished_at < task.created_at:
                raise RestFrameWorkValidationError("Finished date cannot be earlier than created date.")
        return super(MangeTaskBySeniorOrManager, self).update(request, *args, **kwargs)



class UserManageTaskViewSet(viewsets.ModelViewSet):
    """Junior user just can see tasks with fields of attached and progress"""
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilterSet
    serializer_class = TaskUserSerializer
    permission_classes = [IsPutPatchOrGet,IsAuthenticated]

    def get_queryset(self):
        print(self.request.user)
        user = self.request.user
        if user.current_project.project_manager==user:
            return Task.objects.filter(project=user.current_project)
        tasks  = Task.objects.filter(Q(assigned=user) | Q(creator=user) ,project=user.current_project).all()
        return tasks

    def retrieve(self, request, *args, **kwargs):

        task = self.get_queryset().filter(id=kwargs['pk']).first()

        assign_id = task.assigned.id if task.assigned else None
        project_id = task.project.id if task.project else None


        label=Role.objects.filter(project_id=project_id,user_id=assign_id).first().skill
        kwargs['context'] = {
            **self.get_serializer_context(),
            'label':label
        }

        serializer = self.get_serializer(task, many=False, context={'label':label.id})

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self,*args, **kwargs):


        if self.action == "list":
            return TaskSerializerRead
        if self.action =="retrieve":

            return TaskSerializerReadSingle


        return super().get_serializer_class()


class CreateTaskCategory(mixins.CreateModelMixin,viewsets.GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = TaskCategorySerializer

class UpdateCategoryToTaskViewSet(mixins.UpdateModelMixin,viewsets.GenericViewSet):
    serializer_class = UpdateTaskCategorySerializer


class GetUserLevel(mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    serializer_class = GetUserLevelSerializer
    queryset = User.objects.all()





class CreateSkill(viewsets.ModelViewSet):
    serializer_class = SkillSerializer
    permission_classes = [PermissionPM]
    def get_queryset(self):
        return Skill.objects.filter(project=self.request.user.current_project)

class RoleViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    permission_classes = [PermissionPM]
    serializer_class = RoleSerializer
    def get_queryset(self, *args, **kwargs):
        project_id = self.request.user.current_project 
        return Role.objects.filter(project=project_id)
    
class InviteUserViewSet(viewsets.ViewSet):
    permission_classes = [PermissionPM]
    def retrieve(self, request, *args, **kwargs):
        project = get_object_or_404(Project,id=self.kwargs.get('project_pk'))

        skills = Skill.objects.filter(project_id=self.kwargs['project_pk'])
        serializer = SkillSerializer(skills, many=True)
        
        level = [[3,'کارمند عادی'], [2,'کارمند ارشد']]
        data = {
            'project': project.title,
            'level': level,
            'skills': serializer.data
            
        }
        
        return Response(data, status=status.HTTP_200_OK)


    def create(self, request, **kwargs):    
        inviter_email = self.request.user.email
        to_email = request.data.get('to_email')
        project = get_object_or_404(Project,id=self.kwargs.get('project_pk'))
        skill = get_object_or_404(Skill, id=request.data.get('skill'))
        level=request.data.get('level')
        try:
            validate_email(to_email)
            validate_email(inviter_email)
            islogin=0
            if User.objects.filter(email=to_email).exists()== False:
                islogin=1

                user = User.objects.create(email=to_email, password=make_password(to_email),current_project=project)
                print(user)
            
            users_project = project.users.all()            

            if users_project.filter(email=to_email).exists() or project.project_manager.email == to_email :
                return Response({'message': 'این کاریر در پروژه عضو است'}, status=status.HTTP_400_BAD_REQUEST)
            user = get_object_or_404(User, email=to_email)
            project.users.add(user)
            Role.objects.create(user=get_object_or_404(User,email=to_email), project=project, skill=skill, level=level)
                
            send_invitation_email(inviter_email, to_email, project=project, project_id=self.kwargs['project_pk'], level=level, skill=skill.name,islogin=islogin)
            return Response({'message': 'ایمیل دعوت ارسال شد.'}, status=status.HTTP_200_OK)
        except ValidationError:
            raise exceptions.ValidationError('آدرس ایمیل نامعتبر است.')

class AcceptInviteUserViewSet(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        return Response({'message': 'شما با موفقیت در پروژه شرکت کردید'}, status=status.HTTP_200_OK)


class GetLevelSkillView(APIView):
    def get(self, request, **kwargs):
        project_id = request.user.current_project
        user=request.user.id

        if Project.objects.filter(id=project_id.id,project_manager_id=user).exists():
            return Response({'level': 1, 'skill': 'مدیر پروژه'},  status.HTTP_200_OK)
        role = Role.objects.filter(project_id=project_id, user_id=user).first()

        return Response({'level':role.level,'skill':role.skill.name}, status.HTTP_200_OK)


class ListUserViewSet(viewsets.ReadOnlyModelViewSet):
    def get_queryset(self, *args, **kwargs):
        project = get_object_or_404(Project, id=self.kwargs['project_pk'])
        users = project.users.all()
        return  users
    serializer_class = UserListProjectSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'project_id': self.kwargs['project_pk']})

        return Response(serializer.data, status=status.HTTP_200_OK)

class GetUsersWithSkillView(generics.ListAPIView):
    """get skill id and current logged user(manager) project and return users in the same field """
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        project_id = self.request.user.current_project.id
        skill_id = self.kwargs.get('skill_id')

        if not project_id or not skill_id:
            raise RestFrameWorkValidationError("هم نیاز به پروژه هست هم به لیبل حرفه ")
        users = User.objects.filter(
            role__project_id=project_id,
            role__skill_id=skill_id
        ).distinct()

        return users
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class DeleteUserProjectViewSets(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    serializer_class = UserListProjectSerializer
    permission_classes = [IsAuthenticated, PermissionPM]
    
    def get_queryset(self, *args, **kwargs):
        project_id = self.request.user.current_project.id
        return Project.objects.filter(pk=project_id).first().only('users')
    
    def delete(self, request, *args, **kwargs):
        project_id = self.request.user.current_project.id    
        project = Project.objects.filter(pk=project_id).first()
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        if user in project.users.all():
            project.users.remove(user)
            user.current_project=None
            user.save()
            role = get_object_or_404(Role, user_id = user_id)
            role.delete()
            return Response({'message': 'کاربر مورد نظر با موفقیت از پروژه حذف شد'}, status=status.HTTP_204_NO_CONTENT)
        return Response({'message': 'کاربر مورد نظر در پروژه شرکت ندارد'}, status=status.HTTP_404_NOT_FOUND)