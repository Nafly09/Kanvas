from pkg_resources import require
from rest_framework import serializers
from kanvas.users.serializers import UsersSerializers


class CourseSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    demo_time = serializers.TimeField()
    link_repo = serializers.CharField()
    instructor = UsersSerializers(required=False)
    students = UsersSerializers(many=True, required=False)


class InstructorSerializer(serializers.Serializer):
    instructor_id = serializers.CharField()


class StudentSerializer(serializers.Serializer):
    students_id = serializers.ListField(child=serializers.CharField())
