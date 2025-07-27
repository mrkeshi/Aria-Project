from django.db.models.fields import return_None
from djoser.serializers import UserSerializer as BaseUserSerializer,\
  UserCreateSerializer as BaseUserCreateSerializer,\
  UserCreatePasswordRetypeSerializer as BaseUserCreatePasswordRetypeSerializer\

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as BaseTokenObtainPairSerializer

from rest_framework import serializers, exceptions
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserSerializer(BaseUserSerializer):
  class Meta:
    model = User
    fields = ['id','email', 'avatar', 'first_name', 'last_name', 'phone_number','current_project', 'is_active', 'last_login','about' ]


class CustomUserCreateSerializer(BaseUserCreateSerializer):
  class Meta:
    model = User
    fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'last_login' ]

  def create(self, validated_data):
    user = User(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user

class CustomUserCreatePasswordRetypeSerializer(BaseUserCreatePasswordRetypeSerializer):
  class Meta(BaseUserCreatePasswordRetypeSerializer.Meta):
    model = User
    fields = ['email', 'first_name', 'last_name', 'phone_number', 'password', 'last_login']



class CustomTokenObtainPairSerializer(BaseTokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)
    return token

  def validate(self, attrs):
    email = attrs.get('email')
    password = attrs.get('password')
    try:
      user = User.objects.get(email=email)
      if not user.check_password(password):
        raise exceptions.AuthenticationFailed('ایمیل با رمز ورود مطابقت ندارد')
    except User.DoesNotExist:
      raise exceptions.AuthenticationFailed('کاربر وجود ندارد')


    return super().validate(attrs)

class UserNameSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
      model = User
      fields = ['id', 'name']

    def get_name(self, obj):
      if obj.first_name:
        return obj.first_name+" "+obj.last_name
      return obj.email