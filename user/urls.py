from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from user import views


urlpatterns = [
    path("register", views.UserRegister.as_view()),
    path("auth", TokenObtainPairView.as_view()),
    path("auth/refresh", TokenRefreshView.as_view()),
    path("auth/verify", TokenVerifyView.as_view()),
]
