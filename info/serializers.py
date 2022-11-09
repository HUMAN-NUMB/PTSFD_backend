from django.contrib.auth import get_user_model
from rest_framework import serializers

from info.models import Info


User = get_user_model()


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        exclude = ["user"]
