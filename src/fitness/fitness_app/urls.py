from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="login"),
    path("home", views.home, name="login"),
    path("contact", views.contact, name="contact"),
    path("gallery", views.gallery, name="gallery"),
    path("about", views.about, name="about"),
    path("portal", views.portal, name="portal"),
    path(
        "beginners_routines", views.beginners_routines, name="beginners_routines"
    ),
    path("trainers_list", views.trainers_list, name="trainers_list")
]