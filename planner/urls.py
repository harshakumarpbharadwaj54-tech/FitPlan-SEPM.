from django.urls import path

from . import views, weekly_views

urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("workouts/", views.workout_list, name="workout_list"),
    path("meals/", views.meal_list, name="meal_list"),
    path("weekly-plan/", weekly_views.weekly_plan_view, name="weekly_plan"),
]
