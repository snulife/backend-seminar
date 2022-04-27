from django.contrib.auth.models import User
from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    description = models.CharField(max_length=200, blank=True)
    price = models.PositiveIntegerField(null=True)


class SurveyResult(models.Model):
    EXPERIENCE_DEGREE = (
        (1, 'very low'),
        (2, 'low'),
        (3, 'middle'),
        (4, 'high'),
        (5, 'very_high'),
    )

    user = models.ForeignKey(User, null=True, related_name='surveys', on_delete=models.SET_NULL)
    os = models.ForeignKey(OperatingSystem, null=True, related_name='surveys', on_delete=models.SET_NULL)
    python = models.PositiveSmallIntegerField(choices=EXPERIENCE_DEGREE)
    rdb = models.PositiveSmallIntegerField(choices=EXPERIENCE_DEGREE)
    programming = models.PositiveSmallIntegerField(choices=EXPERIENCE_DEGREE)
    major = models.CharField(max_length=100, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    backend_reason = models.CharField(max_length=500, blank=True)
    waffle_reason = models.CharField(max_length=500, blank=True)
    say_something = models.CharField(max_length=500, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
