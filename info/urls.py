from django.urls import path

from info import views


urlpatterns = [
    path("", views.InfoView.as_view()),
]
