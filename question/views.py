from rest_framework import generics

from question.models import Question
from question.serializers import QuestionSerializers

# Create your views here.
class QuestionAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers
