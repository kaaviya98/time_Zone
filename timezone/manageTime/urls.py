from django.urls import path
from . import views

app_name = "manageTime"

urlpatterns = [
    path("", views.display, name="display"),
    path("change/", views.set_timezone, name="set_timezone"),
]