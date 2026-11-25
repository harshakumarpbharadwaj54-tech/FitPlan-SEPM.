from django.contrib import admin
from django.urls import include, path

from planner.auth_views import signup_view


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/signup/", signup_view, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", include("planner.urls")),
]
