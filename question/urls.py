from django.urls import path

from question import views


urlpatterns = [
    path("", views.QuestionAPIView.as_view()),
]
