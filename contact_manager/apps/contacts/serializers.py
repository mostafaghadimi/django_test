from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

from apps.contacts.models import Contact
from apps.users.models import User


class ContactSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='owner')


    class Meta:
        model = Contact
        fields = ['id', 'owner', 'name', 'description']
        read_only_fields = ['owner']

