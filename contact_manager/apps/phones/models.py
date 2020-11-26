from django.db import models

# Create your models here.
from apps.contacts.models import Contact


class Phones(models.Model):
    person = models.ForeignKey(
        Contact,
        related_name="phones",
        on_delete=models.CASCADE,
    )

    phone_no = models.CharField(
        max_length=11,
    )