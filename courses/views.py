from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_422_UNPROCESSABLE_ENTITY,
)


from courses.serializers import CourseSerializer
from courses.models import Courses
from courses.permissions import IsInstructor


class CoursesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]

    def post(self, request: Request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_course = Courses.objects.filter(name=request.data["name"]).exists()

        if found_course:
            return Response(
                {"Message": "Requested Course already exists"},
                HTTP_422_UNPROCESSABLE_ENTITY,
            )

        course = Courses.objects.create(**serializer.validated_data)
        serializer = CourseSerializer(course)

        return Response(serializer.data, HTTP_201_CREATED)

    def get(self, _: Request):
        found_courses = Courses.objects.all()
        serializer = [CourseSerializer(course).data for course in found_courses]
        return Response(serializer)
