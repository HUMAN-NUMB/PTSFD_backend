from django.urls import re_path

from info import views


urlpatterns = [
    re_path(r"^(?P<user_id>\w+$)", views.InfoViewSet.as_view()),
]
