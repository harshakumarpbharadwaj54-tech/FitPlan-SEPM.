from django.contrib import admin

from .models import Meal, PlanItem, Profile, WeeklyPlan, Workout


admin.site.register([Profile, Workout, Meal, WeeklyPlan, PlanItem])
