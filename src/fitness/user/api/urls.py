from django.urls import path, re_path
from .views import CurrentTraineeAPIView

urlpatterns = [
    path("trainee/", CurrentTraineeAPIView.as_view(), name="trainee"),
    # TODO
    # path("trainer/", CurrentTrainerAPIView, name="trainer"),
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]