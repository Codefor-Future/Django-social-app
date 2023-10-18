from django.urls import path
from .views import dashboard,profile_list,profile_page

app_name = "socialapp"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("profiles", profile_list, name="profile_list"),
    path("profile/<int:pk>", profile_page, name="profile_page")
]
