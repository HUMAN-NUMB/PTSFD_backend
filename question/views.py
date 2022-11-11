from rest_framework import generics
from django.db.models.query import QuerySet

from question.models import Question, AdvancedQuestion
from question.serializers import QuestionSerializers

# Create your views here.
class QuestionAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializers

    def get_queryset(self):
        if self.request.headers.get("Advanced"):
            queryset = AdvancedQuestion.objects.all()
        else:
            queryset = Question.objects.all()

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
