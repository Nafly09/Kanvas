from django.urls import path

from courses.views import CoursesView

urlpatterns = [
    path("courses/", CoursesView.as_view()),
]
