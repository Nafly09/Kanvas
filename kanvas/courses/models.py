from uuid import uuid4

from django.db import models


class Courses(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(null=False, max_length=155, unique=True)
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    demo_time = models.TimeField()
    link_repo = models.CharField(max_length=155)
    instructor = models.OneToOneField(
        "users.Users",
        on_delete=models.SET_NULL,
        related_name="current_instructor",
        null=True,
        default=None,
    )
    students = models.ManyToManyField(
        "users.Users", related_name="inlisted_courses")
