from django.urls import include, path
from rest_framework import routers

from apps.users.views import UserList

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('all/', UserList.as_view()),
    path('register/', UserList.as_view()),
    path('login/', TokenObtainPairView.as_view()),
]
