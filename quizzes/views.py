from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Quiz, QuizAttempt
from .serializers import (
    QuizSerializer,
    QuizAttemptSerializer
)


class QuizDetailView(generics.RetrieveAPIView):

    queryset = Quiz.objects.all()

    serializer_class = QuizSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]


class SubmitQuizView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request, quiz_id):

        quiz = Quiz.objects.get(
            id=quiz_id
        )

        answers = request.data.get(
            "answers",
            {}
        )

        questions = quiz.questions.all()

        score = 0

        for question in questions:

            answer = answers.get(
                str(question.id)
            )

            if answer == question.correct_answer:
                score += 1

        total = questions.count()

        attempt = QuizAttempt.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            total_questions=total
        )

        return Response({
            "message": "Quiz submitted successfully",
            "score": score,
            "total": total,
            "percentage":
                round((score / total) * 100, 2)
                if total else 0,
            "attempt_id": attempt.id
        })


class MyQuizAttemptsView(generics.ListAPIView):

    serializer_class = QuizAttemptSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):

        return QuizAttempt.objects.filter(
            student=self.request.user
        ).order_by("-attempted_at")
