from django.urls import path

from . import views


urlpatterns = [
    path("profile/", views.profile_view, name="profile"),
    path("workouts/", views.workout_list, name="workout_list"),
    path("meals/", views.meal_list, name="meal_list"),
]
