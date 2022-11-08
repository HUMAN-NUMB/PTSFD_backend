from rest_framework import generics

from info.models import Info
from info.serializers import InfoSerializers


class InfoView(generics.ListAPIView, generics.UpdateAPIView):
    queryset = Info.objects
    serializer_class = InfoSerializers
    lookup_field = "user"
    lookup_url_kwarg = "user_id"
