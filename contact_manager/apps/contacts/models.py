from django.db import models


# Create your models here.
from apps.users.models import User


class Contact(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    name = models.CharField(
        max_length=70
    )
    description = models.TextField()
