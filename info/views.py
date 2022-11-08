from rest_framework import generics
from rest_framework import permissions

from info.models import Info
from info.serializers import InfoSerializers


class InfoViewSet(generics.ListAPIView, generics.UpdateAPIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Info.objects.all()
    serializer_class = InfoSerializers
