from django.urls import path
from .views import run_tasks

urlpatterns = [
    path("run-tasks/", run_tasks),
]
