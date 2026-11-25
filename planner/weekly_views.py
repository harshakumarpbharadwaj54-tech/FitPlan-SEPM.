from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import WeeklyPlan
from .services import create_weekly_plan


@login_required
def weekly_plan_view(request):
    if request.method == "POST":
        create_weekly_plan(request.user)
        return redirect("weekly_plan")

    plan = (
        WeeklyPlan.objects.filter(user=request.user)
        .prefetch_related("items")
        .order_by("-week_start")
        .first()
    )

    return render(
        request,
        "planner/weekly_plan.html",
        {"plan": plan},
    )
