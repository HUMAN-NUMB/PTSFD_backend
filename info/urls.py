from django.urls import re_path

from info import views


urlpatterns = [
    re_path(r"", views.InfoViewSet.as_view()),
]
