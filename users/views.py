from urllib import response
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.decorators import APIView
from rest_framework.authentication import TokenAuthentication
from users.permissions import IsAdmin
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_422_UNPROCESSABLE_ENTITY, HTTP_201_CREATED, HTTP_401_UNAUTHORIZED, HTTP_403_FORBIDDEN, HTTP_204_NO_CONTENT)

from users.serializers import AddressSerializer, LoginSerializer, UsersSerializers
from users.models import (Users, Address)


class UsersView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]

    def get(self, request: Request):
        serializer = UsersSerializers(request.user)
        if not serializer.data['is_admin']:
            return Response({"detail": "You do not have permission to perform this action."}, HTTP_403_FORBIDDEN)
        found_users = Users.objects.all()
        serializer = [UsersSerializers(user).data for user in found_users]
        return Response(serializer)

    def post(self, request: Request):
        serializer = UsersSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_user = Users.objects.filter(
            email=serializer.validated_data["email"]).exists()

        if found_user:
            return Response({"message": "User already exists"}, HTTP_422_UNPROCESSABLE_ENTITY)
        user = Users.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])
        user.save()
        serializer = UsersSerializers(user)

        return Response(serializer.data, HTTP_201_CREATED)

    def delete(self, request: Request):
        serializer = UsersSerializers(request.user)
        Users.objects.filter(email=serializer.data["email"]).delete()
        return Response('', HTTP_204_NO_CONTENT)


class AddressView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]

    def put(self, request: Request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        address, _ = Address.objects.get_or_create(
            **serializer.validated_data)
        address.users.add(request.user)
        serializer = AddressSerializer(address)
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username=serializer.validated_data["email"],
            password=serializer.validated_data["password"],
        )

        if not user:
            return Response({"message": "Invalid Credentials"}, HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
