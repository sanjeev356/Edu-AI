from django.urls import path

from .views import (
    QuizDetailView,
    SubmitQuizView,
    MyQuizAttemptsView
)

urlpatterns = [

    path(
        "<int:pk>/",
        QuizDetailView.as_view()
    ),

    path(
        "<int:quiz_id>/submit/",
        SubmitQuizView.as_view()
    ),

    path(
        "my-attempts/",
        MyQuizAttemptsView.as_view()
    ),
]