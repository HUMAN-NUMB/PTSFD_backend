from rest_framework import serializers

from question.models import BasicQuestion


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicQuestion
        exclude = []
