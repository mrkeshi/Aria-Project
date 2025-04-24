from django.contrib.auth import get_user_model
from django.db.models import Avg
from rest_framework.response import Response

from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, status

from core.serializers import CustomUserSerializer
from .models import *

User = get_user_model()


class UserListProjectSerializer(ModelSerializer):
    skill = serializers.SerializerMethodField(method_name='get_skill')
    level = serializers.SerializerMethodField(method_name='get_level')
    number_of_tasks = serializers.SerializerMethodField(method_name='get_number_of_tasks', read_only=True)
    average_rate_of_all_tasks = serializers.SerializerMethodField(method_name='get_rate_of_all_tasks', read_only=True)
    countTask = serializers.SerializerMethodField(method_name='get_count_task', read_only=True)
    skill_id = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'skill_id', 'email', 'skill', 'level', 'number_of_tasks',
                  'average_rate_of_all_tasks', 'countTask', 'last_login']

    def get_skill_id(self, user):
        id = self.context.get('project_id')
        role = Role.objects.filter(user=user, project=id).first()
        if (role):
            return role.id
        return "بدون فیلد"

    def get_count_task(self, user: User):
        tasks = Task.objects.filter(project=self.context.get('project_id'), assigned=user).count()
        return tasks

    def get_rate_of_all_tasks(self, user: User):
        sum_rate = 0
        tasks = Task.objects.filter(project=self.context.get('project_id'), assigned=user)
        for task in tasks:
            if task.progress is None:
                continue
            sum_rate += task.progress

        if tasks.count() == 0:
            return 0
        average_rate = sum_rate / tasks.count()

        return average_rate % 100

    def get_number_of_tasks(self, user: User):
        number_of_tasks = Task.objects.filter(project=self.context.get('project_id'), assigned=user).count()
        return number_of_tasks

    def get_skill(self, user: User):
        id = self.context.get('project_id')
        role = Role.objects.filter(user=user, project=id).first()
        if (role.skill):
            return role.skill.name
        return "بدون فیلد"

    def get_level(self, user: User):
        id = self.context.get('project_id')
        role = Role.objects.filter(user=user, project=id).first()
        return role.level


class TaskSerializer(ModelSerializer):
    # TODO: we need to make relation to creator and user who attend

    attached = serializers.FileField(allow_null=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['creator', 'assigned_attached', 'done']


class TaskSerializerRead(ModelSerializer):
    attached = serializers.FileField(allow_null=True, required=False)
    creator = CustomUserSerializer()
    assigned = CustomUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['creator', 'assigned_attached', 'done']


class TaskSerializerReadSingle(ModelSerializer):
    attached = serializers.FileField(allow_null=True, required=False)
    creator = CustomUserSerializer()
    assigned = CustomUserSerializer(read_only=True)
    label = serializers.SerializerMethodField()
    finished_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['creator', 'assigned_attached', 'done']

    def get_label(self, obj):
        return self.context.get('label')


class TaskUpdateSerializer(ModelSerializer):
    attached = serializers.FileField(allow_null=True, required=False)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['creator', 'assigned_attached', 'done']


# class ListProjectSerializer(ModelSerializer):

#     class Meta:
#         model = Project
#         fields = ['id', 'title', 'description','level']
class ProjectSerializer(ModelSerializer):
    average_rate = serializers.SerializerMethodField(method_name='get_average_rate', read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'status', 'average_rate']
        read_only_fields = ['project_manager']

    def get_average_rate(self, project: Project):
        sum_rate = 0
        tasks = Task.objects.filter(project=project.id)
        if tasks.count() == 0:
            return 0
        for task in tasks:
            if task.progress is None:
                continue
            sum_rate += task.progress

        average_rate = sum_rate / tasks.count()
        return average_rate % 100


# TODO: this is need to add user
class TaskCategorySerializer(ModelSerializer):
    class Meta:
        model = TaskCategories
        fields = ['category', 'project_name']


class TaskDoneSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'done']


class UpdateTaskCategorySerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['project', 'category']


class GetUserLevelSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ['level']


class SkillSerializer(ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
        user = self.context['request'].user
        current_project = user.current_project
        skill = Skill.objects.create(**validated_data, project=current_project)
        return skill


class RoleSerializer(ModelSerializer):
    skill_name = serializers.CharField(source='skill.name', read_only=True)
    level_name = serializers.CharField(source='get_level_display', read_only=True)
    user = serializers.IntegerField(source='user.id', read_only=True)
    project = serializers.IntegerField(source='project.id', read_only=True)
    user_email = serializers.CharField(source='user.email', read_only=True)
    user_name = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Role
        fields = '__all__'


class TaskUserSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['creator',
                            'assigned',
                            'created_at',
                            'updated_at',
                            'finished_at',
                            'review',
                            'importance',
                            'owner_note',
                            'done',
                            'project',
                            'rate',
                            'description',
                            'attached',
                            'title',
                            'category',
                            ]


class TaskSeniorUserSerializer(ModelSerializer):
    creator = CustomUserSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = [
            'created_at',
            'Category',
        ]


class UserProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  # Nest RoleSerializer

    class Meta:
        model = User
        fields = ['role']


class ProjectDetailsSerializer(serializers.Serializer):
    developers_of_project = serializers.IntegerField(read_only=True)
    project_task_count = serializers.IntegerField(read_only=True)
    user_projects = serializers.IntegerField(read_only=True)


class ReportingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'rate']


class CompletedTaskIn10DaysAgoSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()


class Top4UserInProjectSerializer(serializers.ModelSerializer):
    count_of_task_user_completed = serializers.SerializerMethodField(method_name='get_count_of_task_user_completed')
    average_score_for_tasks = serializers.SerializerMethodField(method_name='get_average_score_for_tasks')
    user_role = serializers.SerializerMethodField(method_name='get_user_current_role')

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'user_role', 'average_score_for_tasks',
                  'count_of_task_user_completed', 'avatar']

    def get_count_of_task_user_completed(self, user):
        project_id = self.context.get('project_id')
        count_of_task_user_completed = Task.objects.filter(assigned=user, project_id=project_id, done=True).count()
        return count_of_task_user_completed

    def get_average_score_for_tasks(self, user):
        project_id = self.context.get('project_id')
        get_average_score_for_tasks = Task.objects.filter(assigned=user, project_id=project_id, done=True) \
            .aggregate(AverageScoreOfTasks=Avg('rate'))['AverageScoreOfTasks']
        return get_average_score_for_tasks

    def get_user_current_role(self, user):
        project_id = self.context.get('project_id')
        role = Role.objects.filter(user=user, project_id=project_id).first()
        return role.level


class SkillTaskCountViewSerializer(serializers.Serializer):
    task_count = serializers.IntegerField()
    skill_name = serializers.CharField(source='assigned__role__skill__name')


class UserProfileSerializer(serializers.ModelSerializer):
    role = RoleSerializer()  # Nest RoleSerializer

    class Meta:
        model = User
        fields = ['role']


class ProjectDetailsSerializer(serializers.Serializer):
    developers_of_project = serializers.IntegerField(read_only=True)
    project_task_count = serializers.IntegerField(read_only=True)
    user_projects = serializers.IntegerField(read_only=True)


class ReportingTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'progress']


class CompletedTaskIn10DaysAgoSerializer(serializers.Serializer):
    date = serializers.DateField()
    count = serializers.IntegerField()


class Top4UserInProjectSerializer(serializers.ModelSerializer):
    count_of_task_user_completed = serializers.SerializerMethodField(method_name='get_count_of_task_user_completed')
    average_score_for_tasks = serializers.SerializerMethodField(method_name='get_average_score_for_tasks')
    user_role = serializers.SerializerMethodField(method_name='get_user_current_role')
    email=serializers.EmailField(read_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name','email', 'user_role', 'average_score_for_tasks',
                  'count_of_task_user_completed', 'avatar']

    def get_count_of_task_user_completed(self, user):
        project_id = self.context.get('project_id')
        count_of_task_user_completed = Task.objects.filter(assigned=user, project_id=project_id, done=True).count()
        return count_of_task_user_completed

    def get_average_score_for_tasks(self, user):
        project_id = self.context.get('project_id')
        get_average_score_for_tasks = Task.objects.filter(assigned=user, project_id=project_id, done=True) \
            .aggregate(AverageScoreOfTasks=Avg('rate'))['AverageScoreOfTasks']
        return get_average_score_for_tasks

    def get_user_current_role(self, user):
        project_id = self.context.get('project_id')
        role = Role.objects.filter(user=user, project_id=project_id).first()
        return role.level


class SkillTaskCountViewSerializer(serializers.Serializer):
    task_count = serializers.IntegerField()
    skill_name = serializers.CharField(source='assigned__role__skill__name')