from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from django.db.models.query import QuerySet

from score.models import Score
from score.serializers import ScoreSerializers


class ScoreAPIView(generics.CreateAPIView, generics.ListAPIView):
    serializer_class = ScoreSerializers

    def perform_create(self, serializer):
        user = self.request.user
        times = Score.objects.filter(user=user).count() + 1
        serializer.save(user=user, times=times)

    def get_queryset(self):
        user = self.request.user
        queryset = Score.objects.filter(user=user).all()
        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset
