from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import PlanItem, Profile, WeeklyPlan
from .services import create_weekly_plan


class WeeklyPlanServiceTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="fitplan-test-user",
            password="test-password-123",
        )
        Profile.objects.create(
            user=self.user,
            available_days=["monday", "wednesday"],
        )

    def test_creates_seven_day_reviewable_draft(self):
        plan = create_weekly_plan(self.user, week_start=date(2025, 1, 6))

        self.assertEqual(plan.status, WeeklyPlan.Status.NEEDS_REVIEW)
        self.assertFalse(plan.ai_generated)
        self.assertEqual(plan.items.count(), 7)

        monday = plan.items.get(day=PlanItem.Day.MONDAY)
        tuesday = plan.items.get(day=PlanItem.Day.TUESDAY)

        self.assertFalse(monday.is_rest_day)
        self.assertTrue(tuesday.is_rest_day)

    def test_requires_monday_week_start(self):
        with self.assertRaises(ValueError):
            create_weekly_plan(self.user, week_start=date(2025, 1, 7))
