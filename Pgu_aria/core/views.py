from django.shortcuts import render
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet , ViewSet
from .serializers import CustomTokenObtainPairSerializer,UserNameSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import mixins, status

from rest_framework import viewsets
from . import serializers
# Create your views here.
User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
  serializer_class = CustomTokenObtainPairSerializer


  class UserProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
      user = request.user

      email = request.data.get('email', None)
      first_name = request.data.get('first_name', None)
      last_name = request.data.get('last_name', None)
      phone_number = request.data.get('phone_number', None)


      avatar = request.FILES.get('avatar', None)

      if email:
        user.email = email
      if first_name:
        user.first_name = first_name
      if last_name:
        user.last_name = last_name
      if phone_number:
        user.phone_number = phone_number
      if avatar:
        user.avatar = avatar

      user.save()
      user.userprofile.save()  #

      return Response({"message": "Profile updated successfully!"}, status=status.HTTP_200_OK)

class GetUserNameView(APIView):
    def get(self, request, user_id):
      try:
        user = User.objects.get(id=user_id)

        serializer = UserNameSerializer(user)
        return Response(serializer.data)
      except User.DoesNotExist:
        raise NotFound({"detail": "User not found"})


