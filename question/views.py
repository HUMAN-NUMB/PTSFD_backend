from rest_framework import generics
from django.db.models.query import QuerySet

from question.models import BasicQuestion, AdvancedQuestion
from question.serializers import QuestionSerializers


class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializers

    def get_queryset(self):
        if self.request.data.get("Advance", default=None):
            queryset = AdvancedQuestion.objects.all()
        else:
            queryset = BasicQuestion.objects.all()

        if isinstance(queryset, QuerySet):
            queryset = queryset.all()
        return queryset
