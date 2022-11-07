from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["user_id", "last_login", "username", "password"]
        read_only_fields = [
            "user_id",
            "last_login",
        ]

    def save(self, **kwargs):
        user = super(UserSerializers, self).save(**kwargs)
        user.set_password(self.data["password"])
        user.save()
        return user
