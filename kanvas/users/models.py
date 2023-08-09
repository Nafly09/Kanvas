from uuid import uuid4

from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    email = models.EmailField(unique=True)
    username = models.CharField(unique=False, null=True, max_length=255)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    address = models.ForeignKey(
        "users.Address", on_delete=models.SET_NULL, related_name="users", null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Address(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    zip_code = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
