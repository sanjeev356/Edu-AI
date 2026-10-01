from rest_framework import serializers
from .models import Quiz, Question, QuizAttempt


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question

        fields = [
            "id",
            "question_text",
            "option_a",
            "option_b",
            "option_c",
            "option_d",
        ]


class QuizSerializer(serializers.ModelSerializer):

    questions = QuestionSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Quiz

        fields = [
            "id",
            "title",
            "course",
            "questions",
        ]


class QuizAttemptSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuizAttempt

        fields = [
            "id",
            "quiz",
            "score",
            "total_questions",
            "attempted_at",
        ]