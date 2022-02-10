from django.shortcuts import render, redirect
from django.contrib import messages
from django.template.loader import get_template

from .forms import *
from django.core.mail import EmailMultiAlternatives

from fitness import settings


def trainee_register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        trainee_register_form = TraineeRegisterForm(request.POST)
        if form.is_valid() and trainee_register_form.is_valid():
            user = form.save()
            profile = trainee_register_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            ######################### mail system ####################################
            htmly = get_template("user/email.html")
            d = {"username": username}
            subject, from_email, to = (
                "welcome to Fitness",
                settings.EMAIL_HOST_USER,
                email,
            )
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            try:
                msg.send()
            except:
                # TODO - create 404 pages
                print("email not working")
                pass
            ##################################################################
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("index")
    else:
        form = UserRegisterForm()
        trainee_form = TraineeRegisterForm()

    return render(request, "user/trainee_register.html", {"form": form, "trainee_form": trainee_form})


def trainer_register(request):
    # TrainerRegisterForm
    if request.method == "POST":
        # TODO - update trainer information
        pass
    else:
        form = UserRegisterForm()
        trainer_form = TrainerRegisterForm()

    return render(request, "user/trainer_register.html", {"form": form, "trainer_form": trainer_form})
