from django.urls import path

from courses.views import CoursesView, FilterCourses

urlpatterns = [
    path("courses/", CoursesView.as_view()),
    path("courses/<course_id>/", FilterCourses.as_view()),
]
