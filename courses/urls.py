from django.urls import path

from courses.views import CourseStudentsView, CoursesInstructorsView, CoursesView, CoursesByIdView

urlpatterns = [
    path("courses/", CoursesView.as_view()),
    path("courses/<course_id>/", CoursesByIdView.as_view()),
    path("courses/<course_id>/registrations/students/",
         CoursesInstructorsView.as_view()),
    path("courses/<course_id>/registrations/students/",
         CourseStudentsView.as_view())
]
