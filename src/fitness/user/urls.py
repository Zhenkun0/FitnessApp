from django.urls import path
from . import views
from django.contrib.auth import views as auth

urlpatterns = [
    path("logout/", auth.LogoutView.as_view(template_name="index.html"), name="logout"),
    path("TraineeRegister/", views.trainee_register, name="TraineeRegister"),
    path("TrainerRegister/", views.trainer_register, name="TrainerRegister"),
]
