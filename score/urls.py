from django.urls import path

from score import views


urlpatterns = [
    path("", views.ScoreAPIView.as_view()),
]
