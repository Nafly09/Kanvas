from rest_framework import serializers


class UsersSerializers(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    is_admin = serializers.BooleanField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class AddressSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    zip_code = serializers.CharField(required=True)
    street = serializers.CharField(required=True)
    city = serializers.CharField(required=True)
    state = serializers.CharField(required=True)
    house_number = serializers.CharField(required=True)
    country = serializers.CharField(required=True)
    users = UsersSerializers(many=True, read_only=True)


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()
