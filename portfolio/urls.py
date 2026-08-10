from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.project_archive, name="project_archive"),
    path("projects/<slug:slug>/", views.project_detail, name="project_detail"),
]
