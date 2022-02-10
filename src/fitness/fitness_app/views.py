from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from user.models import *
from .models import *
from .forms import *

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)

        # Register or Update Trainer Info
        if user is not None:
            try:
                trainer = Trainer.objects.get(user=user)
            except:
                trainer = False
            if trainer:
                if trainer.approve:
                    login(request, user)
                    messages.success(request, f" wecome {username} !!")
                    try:
                        trainee = Trainee.objects.filter(trainer_ass=trainer)
                    except:
                        trainee = None
                    print("---------------------------------")
                    data = {"trainee": trainee}
                    return render(request, "TrainerDashBoard.html", data)
                else:
                    messages.success(
                        request, f" wecome {username} please ask admin to approve !!"
                    )
            else:
                login(request, user)
                try:
                    task = Task.objects.filter(
                        person=Trainee.objects.get(user=request.user)
                    )
                except:
                    task = None

                data = {"task": task}
                messages.success(request, f" wecome {username} !!")
                return render(request, "first.html")

        else:
            messages.info(request, f"account done not exit plz sign in")
    if request.user.is_anonymous:
        form = AuthenticationForm()
        return render(request, "index.html", {"form": form})
    else:
        try:
            trainer = Trainer.objects.get(user=request.user)
        except:
            trainer = False
        if trainer:
            if trainer.approve:
                try:
                    trainee = Trainee.objects.filter(trainer_ass=trainer)
                except:
                    trainee = None

                data = {"trainee": trainee}
                return render(request, "TrainerDashBoard.html", data)
            else:
                messages.success(
                    request, f" wecome {username} please ask admin to approve !!"
                )
        else:
            try:
                task = Task.objects.filter(
                    person=Trainee.objects.get(user=request.user)
                )
            except:
                task = None
            data = {"task": task}
            # TODO create home view
            return render(request, "index.html", data)


def about(request):
    return render(request, "about.html")


def gallery(request):
    return render(request, "gallery.html")


def contact(request):
    return render(request, "contact.html")


def portal(request):
    return render(request, "first.html")


def beginners_routines(request):
    return render(request, "beginners_routines.html")
