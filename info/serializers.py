from rest_framework import serializers

from info.models import Info


class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Info
        exclude = ["user"]
