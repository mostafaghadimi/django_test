from rest_framework import viewsets, permissions

from .models import Contact
from .permissions import IsCreator
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsCreator]

    def perform_create(self, serializer):
        return serializer.save(owner = self.request.user)

    def get_permissions(self):
        if self.request.method == "GET":
            self.permission_classes = [IsCreator, permissions.IsAdminUser,]

        if self.request.method == "POST":
            self.permission_classes = [permissions.IsAuthenticated,]

        if self.request.method == "PUT":
            self.permission_classes = [IsCreator]

        if self.request.method == "DELETE":
            self.permission_classes = []

        return super(ContactViewSet, self).get_permissions()