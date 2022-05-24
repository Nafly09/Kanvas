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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
