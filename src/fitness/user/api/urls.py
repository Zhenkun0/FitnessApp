from django.urls import path, re_path
from .views import *
from .serializers import *

urlpatterns = [
    # TODO
    # path("trainee/", TraineeAPIView.as_view(), name="trainee"),
    path('trainee/register/', TraineeRegisterApiView.as_view()),
    # TODO
    # path("trainer/", CurrentTrainerAPIView, name="trainer"),
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]