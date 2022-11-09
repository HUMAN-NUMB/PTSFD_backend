from rest_framework import generics
from django.shortcuts import get_object_or_404

from info.models import Info
from info.serializers import InfoSerializers


class InfoView(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Info.objects
    serializer_class = InfoSerializers
    # lookup_field = "user"
    # lookup_url_kwarg = "user_id"

    # def get_queryset(self):
    #     user_id = self.request.user.user_id
    #     return Info.objects.filter(user=user_id)

    def get_object(self):
        user_id = self.request.user.user_id
        queryset = self.filter_queryset(self.get_queryset()).filter(user=user_id)
        obj = get_object_or_404(queryset)

        self.check_object_permissions(self.request, obj)
        return obj
