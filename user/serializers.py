from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import RefreshToken

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    repassword = serializers.CharField(max_length=512, write_only=True)
    access = serializers.CharField(max_length=256, read_only=True)
    refresh = serializers.CharField(max_length=256, read_only=True)

    class Meta:
        model = User
        fields = ["access", "refresh", "username", "password", "repassword"]
        extra_kwargs = {
            "username": {"write_only": True},
            "password": {"write_only": True},
        }

    def validate(self, attrs):
        if attrs.get("password") != attrs.get("repassword"):
            raise serializers.ValidationError("两次密码不一致！")
        return attrs

    def create(self, validated_data):
        validated_data.pop("repassword")
        user = User.objects.create_user(**validated_data)

        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        refresh = str(refresh)
        user.access = access
        user.refresh = refresh

        return user
