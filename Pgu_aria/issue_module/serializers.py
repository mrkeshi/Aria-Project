from rest_framework import serializers
from urllib3 import request

from workspace_module.models import Role
from issue_module.models import Question, Answer
from workspace_module.serializers import RoleSerializer


class CustomRelatedField(serializers.RelatedField):
    def to_representation(self, value):

        return SimpleAnswerSerializer(value, context=self.context).data

    def to_internal_value(self, data):

        try:
            return Answer.objects.get(pk=data)
        except Answer.DoesNotExist:
            raise serializers.ValidationError("Invalid ID provided.")



class SimpleAnswerSerializer(serializers.ModelSerializer):
    user_role = serializers.SerializerMethodField(method_name='get_user_role', read_only=True)
    respondent_name = serializers.SerializerMethodField(method_name='get_respondent_name', read_only=True)
    creator_avatar = serializers.SerializerMethodField(method_name='get_creator_avatar', read_only=True)
    message_parent=CustomRelatedField(queryset=Answer.objects.all(),required=False, allow_null=True)
    class Meta:
        model = Answer
        fields = ['id', 'question', 'creator_avatar','respondent','respondent_name', 'user_role', 'message_parent', 'description', 'assigned_attached',
                  'created_at',
                  'updated_at',
                  'sub_answers']
        read_only_fields = ['question', 'respondent', 'user_role']

    def get_user_role(self, obj: Answer):
        request = self.context.get('request')

        user_role = Role.objects.get(user=obj.respondent,project=request.user.current_project)
        return RoleSerializer(user_role).data

    # def get_message_parent(self, obj):
    #     if obj.message_parent:
    #         return SimpleAnswerSerializer(obj.message_parent, context=self.context).data
    #     return None
    def get_respondent_name(self, obj: Answer):
        full_name = obj.respondent.get_full_name()
        if full_name.strip() == "" or "NoneNone" in full_name:
            return obj.respondent.email
        return full_name

    def get_creator_avatar(self, obj: Question):
        if obj.respondent and obj.respondent.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.respondent.avatar.url)
            return obj.respondent.avatar.url
        return None

    def create(self, validated_data):
        request = self.context.get('request')
        question_id = request.parser_context['kwargs'].get('question_pk')
        try:
            question = Question.objects.get(pk=question_id)
            if question.status == 2:
                raise serializers.ValidationError("پرسش در حالت یسته قرار دارد و شما نمیتوانید به آن پاسخ دهید")

            validated_data['question'] = question
            validated_data['respondent'] = request.user
            return super().create(validated_data)
        except Question.DoesNotExist:
            raise serializers.ValidationError(' پرسش مد نظر شما وجود ندارد')


class QuestionSerializer(serializers.ModelSerializer):
    answers = SimpleAnswerSerializer(read_only=True, many=True)
    user_role = serializers.SerializerMethodField(method_name='get_user_role', read_only=True)
    task_name = serializers.CharField(source='task.title', read_only=True)
    task_importance = serializers.CharField(source='task.get_importance_display', read_only=True)
    creator_name = serializers.SerializerMethodField(method_name='get_creator_name',read_only=True)

    creator_avatar = serializers.SerializerMethodField(method_name='get_creator_avatar', read_only=True)
    class Meta:
        model = Question
        fields = ['id', 'subject', 'status', 'creator','creator_avatar', 'creator_name', 'user_role', 'description', 'project', 'task', 'task_name', 'task_importance', 'assigned_attached',
                  'created_at',
                  'updated_at', 'answers']
        read_only_fields = ['creator', 'user_role', 'project']

    def get_user_role(self, obj: Question):
        user_role = Role.objects.get(user=obj.creator,project=obj.project)
        return RoleSerializer(user_role).data

    def get_creator_name(self, obj: Question):
        full_name = obj.creator.get_full_name()
        if full_name.strip() == "" or "None None" in full_name:
            return obj.creator.email
        return full_name

    def get_creator_avatar(self, obj: Question):
        if obj.creator and obj.creator.avatar:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.creator.avatar.url)
            return obj.creator.avatar.url
        return None

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['creator'] = request.user
        validated_data['project'] = request.user.current_project
        return super().create(validated_data)
