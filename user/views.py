from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import generics

from user.serializers import UserSerializers

User = get_user_model()


class UserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes = []


class UserBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None
