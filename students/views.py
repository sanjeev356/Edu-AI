from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    RegisterSerializer,
    StudentProfileSerializer
)


class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()

    serializer_class = RegisterSerializer

    permission_classes = [
        permissions.AllowAny
    ]


class StudentProfileView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):

        profile = request.user.student_profile

        serializer = StudentProfileSerializer(profile)

        return Response(serializer.data)

    def put(self, request):

        profile = request.user.student_profile

        serializer = StudentProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)
