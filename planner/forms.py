from django import forms

from .models import Meal, Profile, Workout


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["fitness_goal", "available_days", "preferences"]


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ["activity", "workout_date", "duration_minutes", "notes"]

    def clean_duration_minutes(self):
        duration = self.cleaned_data["duration_minutes"]
        if duration < 1:
            raise forms.ValidationError("Duration must be at least one minute.")
        return duration


class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["description", "meal_date", "notes"]
