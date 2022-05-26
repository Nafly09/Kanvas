from rest_framework import serializers


class UsersSerializers(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(required=True)
    is_admin = serializers.BooleanField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
