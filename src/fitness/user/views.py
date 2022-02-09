from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template

from .forms import *
from django.core.mail import EmailMultiAlternatives

from fitness import settings


def trainee_register(request):
    if request.method == "POST":
        # TODO - update trainee information
        pass
    else:
        form = UserRegisterForm()
        trainee_form = TraineeRegisterForm()

    return render(request, "trainee_register.html", {"form": form, "trainee_form": trainee_form})


def trainer_register(request):
    # TrainerRegisterForm
    if request.method == "POST":
        # TODO - update trainer information
        pass
    else:
        form = UserRegisterForm()
        trainer_form = TrainerRegisterForm()

    return render(request, "trainer_register.html", {"form": form, "trainer_form": trainer_form})

