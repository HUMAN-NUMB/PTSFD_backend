from rest_framework import generics
from django.db.models.query import QuerySet

from question.models import BasicQuestion, AdvancedQuestion
from question.serializers import QuestionSerializers

import json


class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializers

    def get_queryset(self):
        advance = self.request.headers.get("advance")
        # advance = json.loads(self.request.body).get("advance")
        if advance:
            queryset = AdvancedQuestion.objects.all()
        else:
            queryset = BasicQuestion.objects.all()

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset
