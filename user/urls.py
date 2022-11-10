from django.urls import path

from user import views


urlpatterns = [
    path("", views.UserRegister.as_view()),
]
