from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.contacts.views import ContactViewSet

router = DefaultRouter()
router.register('', ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]