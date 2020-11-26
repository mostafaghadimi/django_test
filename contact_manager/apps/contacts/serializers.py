from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.conf import settings
from apps.contacts.models import Contact
from apps.users.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'description', 'owner']



