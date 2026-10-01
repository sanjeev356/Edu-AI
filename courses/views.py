from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Course, Enrollment
from .serializers import (
    CourseSerializer,
    EnrollmentSerializer
)


class CourseListView(generics.ListAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]


class CourseDetailView(generics.RetrieveAPIView):

    queryset = Course.objects.all()

    serializer_class = CourseSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]


class EnrollCourseView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, course_id):

        course = Course.objects.get(
            id=course_id
        )

        enrollment, created = Enrollment.objects.get_or_create(
            student=request.user,
            course=course
        )

        if not created:

            return Response({
                "message": "Already enrolled"
            })

        return Response({
            "message": "Course enrolled successfully"
        })


class MyCoursesView(generics.ListAPIView):

    serializer_class = EnrollmentSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):

        return Enrollment.objects.filter(
            student=self.request.user
        )


class UpdateProgressView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def put(self, request, enrollment_id):

        enrollment = Enrollment.objects.get(
            id=enrollment_id,
            student=request.user
        )

        progress = request.data.get(
            "progress",
            enrollment.progress
        )

        progress = max(
            0,
            min(100, int(progress))
        )

        enrollment.progress = progress

        enrollment.save()

        return Response({
            "message": "Progress updated",
            "progress": progress
        })
