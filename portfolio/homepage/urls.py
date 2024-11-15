from django.urls import path
from . import views

app_name = "homepage"

urlpatterns = [
    path("", view=views.index, name="homepage"),
]