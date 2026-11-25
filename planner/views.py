from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import MealForm, ProfileForm, WorkoutForm
from .models import Meal, Profile, Workout


@login_required
def profile_view(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "planner/profile.html", {"form": form})


@login_required
def workout_list(request):
    if request.method == "POST":
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect("workout_list")
    else:
        form = WorkoutForm()

    workouts = Workout.objects.filter(user=request.user).order_by(
        "-workout_date", "-created_at"
    )
    return render(
        request,
        "planner/workout_list.html",
        {"form": form, "workouts": workouts},
    )


@login_required
def meal_list(request):
    if request.method == "POST":
        form = MealForm(request.POST)
        if form.is_valid():
            meal = form.save(commit=False)
            meal.user = request.user
            meal.save()
            return redirect("meal_list")
    else:
        form = MealForm()

    meals = Meal.objects.filter(user=request.user).order_by(
        "-meal_date", "-created_at"
    )
    return render(
        request,
        "planner/meal_list.html",
        {"form": form, "meals": meals},
    )
