from pkg_resources import require
from rest_framework import serializers
from users.serializers import UsersSerializers


class CourseSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateField(read_only=True)
    demo_time = serializers.TimeField(read_only=True)
    link_repo = serializers.CharField()
    instructor = UsersSerializers(required=False)
    students = UsersSerializers(many=True, required=False)
