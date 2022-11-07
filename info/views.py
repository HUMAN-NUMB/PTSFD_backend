from rest_framework import generics
from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTAuthentication

from info.models import Info
from info.serializers import InfoSerializers


class InfoViewSet(generics.ListAPIView, generics.UpdateAPIView):
    authentication_classes = [
        JWTAuthentication,
    ]
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    queryset = Info.objects.all()
    serializer_class = InfoSerializers
    
