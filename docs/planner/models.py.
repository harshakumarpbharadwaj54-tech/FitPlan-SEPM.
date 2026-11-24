from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="fitplan_profile",
    )
    fitness_goal = models.CharField(max_length=160, blank=True)
    available_days = models.JSONField(default=list, blank=True)
    preferences = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Profile for user {self.user_id}"


class Workout(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="fitplan_workouts",
    )
    activity = models.CharField(max_length=120)
    workout_date = models.DateField()
    duration_minutes = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.activity} on {self.workout_date}"


class Meal(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="fitplan_meals",
    )
    description = models.CharField(max_length=240)
    meal_date = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Meal on {self.meal_date}"


class WeeklyPlan(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACCEPTED = "accepted", "Accepted"
        REJECTED = "rejected", "Rejected"
        NEEDS_REVIEW = "needs_review", "Needs review"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="fitplan_weekly_plans",
    )
    week_start = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    ai_generated = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PlanItem(models.Model):
    class Day(models.TextChoices):
        MONDAY = "monday", "Monday"
        TUESDAY = "tuesday", "Tuesday"
        WEDNESDAY = "wednesday", "Wednesday"
        THURSDAY = "thursday", "Thursday"
        FRIDAY = "friday", "Friday"
        SATURDAY = "saturday", "Saturday"
        SUNDAY = "sunday", "Sunday"

    weekly_plan = models.ForeignKey(
        WeeklyPlan,
        on_delete=models.CASCADE,
        related_name="items",
    )
    day = models.CharField(max_length=9, choices=Day.choices)
    activity = models.CharField(max_length=160, blank=True)
    is_rest_day = models.BooleanField(default=False)
    notes = models.TextField(blank=True)
