from django.urls import path
from .views import *
from rest_framework_nested import routers

urlpatterns = [
    path('jwt/create', CustomTokenObtainPairView.as_view(), name='custom-token-create'),
    path('api/user/<int:user_id>/', GetUserNameView.as_view(), name='get_user_name'),
]

