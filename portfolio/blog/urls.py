from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", view=views.index, name="blog"),
    path("variable/", view=views.variables, name="variable"),
]