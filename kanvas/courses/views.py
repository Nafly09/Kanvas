from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.forms import ValidationError
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
    HTTP_404_NOT_FOUND
)


from kanvas.courses.serializers import CourseSerializer, InstructorSerializer, StudentSerializer
from kanvas.courses.models import Courses
from kanvas.courses.permissions import IsInstructor

from kanvas.users.models import Users


class CoursesView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]

    def post(self, request: Request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_course = Courses.objects.filter(
            name=request.data["name"]).exists()

        if found_course:
            return Response(
                {"message": "Course already exists"},
                HTTP_422_UNPROCESSABLE_ENTITY,
            )

        course = Courses.objects.create(**serializer.validated_data)
        serializer = CourseSerializer(course)

        return Response(serializer.data, HTTP_201_CREATED)

    def get(self, _: Request):
        found_courses = Courses.objects.all()
        serializer = [CourseSerializer(
            course).data for course in found_courses]
        return Response(serializer)


class CoursesByIdView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]

    def get(self, _: Request, course_id: None):
        if not course_id:
            return Response("OMEGALUL")
        try:
            course = Courses.objects.get(uuid=course_id)
            serializer = CourseSerializer(course)
            return Response(serializer.data)
        except ValidationError:
            return Response({"message": "Please inform a valid UUID"}, HTTP_422_UNPROCESSABLE_ENTITY)
        except Courses.DoesNotExist:
            return Response({"message": "Course does not exist"}, HTTP_404_NOT_FOUND)

    def patch(self, request: Request, course_id: None):
        try:
            serializer = CourseSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            if course_id:
                Courses.objects.filter(pk=course_id).update(
                    **serializer.validated_data)
                updated_course = Courses.objects.get(pk=course_id)
                serializer = CourseSerializer(updated_course)
                return Response(serializer.data)
        except IntegrityError:
            return Response({"message": "This course name already exists"}, HTTP_422_UNPROCESSABLE_ENTITY)
        except Courses.DoesNotExist:
            return Response({
                "message": "Course does not exist"
            }, HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({"message": "Please inform a valid UUID"}, HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _, course_id=None):
        try:
            found_course = Courses.objects.filter(pk=course_id).first()

            if not Courses.objects.filter(pk=course_id):
                raise Courses.DoesNotExist

            found_course.delete()

            return Response("", HTTP_204_NO_CONTENT)

        except Courses.DoesNotExist:
            return Response({
                "message": "Course does not exist"
            }, HTTP_404_NOT_FOUND)
        except ValidationError:
            return Response({"message": "Please inform a valid UUID"}, HTTP_422_UNPROCESSABLE_ENTITY)


class CoursesInstructorsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]

    def put(self, request: Request, course_id=None):
        course: Courses = Courses.objects.filter(uuid=course_id)

        if not course.first():
            return Response(
                {"message": "Course does not exist"}, HTTP_404_NOT_FOUND
            )

        serializer = InstructorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_instructor: Users = Users.objects.filter(
            uuid=serializer.validated_data["instructor_id"]
        ).first()

        if not found_instructor:
            return Response(
                {"message": "Invalid instructor_id"}, HTTP_404_NOT_FOUND
            )

        if not found_instructor.is_admin:
            return Response(
                {"message": "Instructor id does not belong to an admin"},
                HTTP_422_UNPROCESSABLE_ENTITY,
            )

        Courses.objects.filter(
            instructor=found_instructor).update(instructor=None)
        course.update(instructor=found_instructor)
        serializer = CourseSerializer(course.first())

        return Response(serializer.data)


class CourseStudentsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsInstructor]

    def put(self, request: Request, course_id=None):

        course = Courses.objects.filter(uuid=course_id).first()

        if not course:
            return Response(
                {"message": "Course does not exist"}, HTTP_404_NOT_FOUND
            )

        serializer = StudentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        students_list = []

        for student_id in serializer.validated_data["students_id"]:
            found_student: Users = Users.objects.filter(
                uuid=student_id).first()
            if not found_student:
                return Response(
                    {"message": "Invalid students_id list"}, HTTP_404_NOT_FOUND
                )
            if found_student.is_admin:
                return Response(
                    {"message": "Some student id belongs to an Instructor"},
                    HTTP_422_UNPROCESSABLE_ENTITY,
                )
            students_list.append(found_student)

        course.students.set(students_list)
        serializer = CourseSerializer(course)

        return Response(serializer.data)
