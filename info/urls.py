from django.urls import path

from info import views


urlpatterns = [
    path("", views.InfoAPIView.as_view()),
]
