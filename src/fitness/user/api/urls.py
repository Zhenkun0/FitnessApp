from django.urls import path, re_path
from rest_framework.routers import DefaultRouter

from .views import *
from .serializers import *

router = DefaultRouter()
router.register("api/auth/users/", TraineeRegisterApiView)

urlpatterns = [
    # TODO
    # path('trainee/register/', TraineeRegisterApiView.as_view()),
    path('profile/', TraineeProfileApiView.as_view({'get': 'retrieve'}))
    # TODO
    # path("trainer/", CurrentTrainerAPIView, name="trainer"),
    # re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]