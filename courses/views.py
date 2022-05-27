from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response

from users.permissions import IsAdmin


class CoursesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdmin]
