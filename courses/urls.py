from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    EnrollCourseView,
    MyCoursesView,
    UpdateProgressView
)

urlpatterns = [

    path(
        "",
        CourseListView.as_view()
    ),

    path(
        "<int:pk>/",
        CourseDetailView.as_view()
    ),

    path(
        "<int:course_id>/enroll/",
        EnrollCourseView.as_view()
    ),

    path(
        "my-courses/",
        MyCoursesView.as_view()
    ),

    path(
        "progress/<int:enrollment_id>/",
        UpdateProgressView.as_view()
    ),
]