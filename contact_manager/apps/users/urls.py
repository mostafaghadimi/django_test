from django.urls import include, path
from rest_framework import routers

from apps.users.views import UserViewSet

# user_list = UserViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })



router = routers.SimpleRouter()
router.register('register', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]
