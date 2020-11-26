from rest_framework import serializers

from apps.contacts.models import Contact
from apps.users.models import User


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    class Meta:
        model = Contact
        fields = ['id', 'owner', 'name', 'description']
        read_only_fields = ['owner']

