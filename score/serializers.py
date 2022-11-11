from rest_framework import serializers

from score.models import Score


class ScoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Score
        exclude = ["id"]
        extra_kwargs = {
            "user": {"write_only": True},
        }
