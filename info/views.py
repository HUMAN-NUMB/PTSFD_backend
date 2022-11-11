from rest_framework import generics
from django.shortcuts import get_object_or_404

from info.models import Info
from info.serializers import InfoSerializers


class InfoAPIView(generics.RetrieveAPIView, generics.UpdateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers
    # lookup_field = "user"
    # lookup_url_kwarg = "user_id"

    # def get_queryset(self):
    #     user_id = self.request.user.user_id
    #     return Info.objects.filter(user=user_id)

    def get_object(self):
        request = self.request
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)
        obj = get_object_or_404(queryset)

        self.check_object_permissions(request, obj)
        return obj
