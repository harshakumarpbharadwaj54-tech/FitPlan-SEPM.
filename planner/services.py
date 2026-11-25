from datetime import date, timedelta

from django.db import transaction

from .models import PlanItem, Profile, WeeklyPlan


@transaction.atomic
def create_weekly_plan(user, week_start=None):
    """Create a reviewable draft using the user's available days."""
    if week_start is None:
        today = date.today()
        week_start = today - timedelta(days=today.weekday())

    if week_start.weekday() != 0:
        raise ValueError("The week must start on a Monday.")

    profile = Profile.objects.filter(user=user).first()
    available_days = set()

    if profile:
        available_days = {
            str(day).lower()
            for day in profile.available_days
            if str(day).lower() in {choice.value for choice in PlanItem.Day}
        }

    plan = WeeklyPlan.objects.create(
        user=user,
        week_start=week_start,
        status=WeeklyPlan.Status.NEEDS_REVIEW,
        ai_generated=False,
    )

    for day in PlanItem.Day:
        is_available = day.value in available_days
        PlanItem.objects.create(
            weekly_plan=plan,
            day=day.value,
            activity="Choose a comfortable activity" if is_available else "",
            is_rest_day=not is_available,
            notes="Draft for user review.",
        )

    return plan
