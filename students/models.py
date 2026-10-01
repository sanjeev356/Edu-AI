from django.db import models

from django.db import models
from django.contrib.auth.models import User


class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    phone = models.CharField(max_length=15, blank=True)
    college = models.CharField(max_length=200, blank=True)
    course = models.CharField(max_length=100, blank=True)
    profile_image = models.URLField(blank=True)

    total_points = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
