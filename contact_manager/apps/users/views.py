from rest_framework import viewsets, permissions

# Create your views here.

from apps.users.models import User
from apps.users.serializers import UserSerializer
from apps.users.permissions import IsCreatorOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = []

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [permissions.IsAuthenticated,]

        if self.request.method == "POST":
            self.permission_classes = [permissions.AllowAny,]

        if self.request.method == "UPDATE":
            self.permission_classes = [permissions.IsAdminUser, IsCreatorOrReadOnly,]

        return super(UserViewSet, self).get_permissions()


