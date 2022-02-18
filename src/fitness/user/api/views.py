from django.shortcuts import render
from rest_framework.permissions import AllowAny

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, mixins, status, viewsets
from djoser import views

from .serializers import *


# Register API
class TraineeRegisterApiView(views.UserViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = TraineeRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trainee = serializer.save()
        return Response({
            "trainee": TraineeRegisterSerializer(trainee, context=self.get_serializer_context()).data,
            "message": "Trainee Created Successfully.  Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)


class TraineeProfileApiView(views.UserViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TraineeRegisterSerializer

    def get(self, request):
        trainee = Trainee.objects.get(user_id=request.user_id)
        return Response({
            "trainee": TraineeRegisterSerializer(trainee, context=self.get_serializer_context()).data,
            "message": "Trainee Created Successfully.  Now perform Login to get your token",
        }, status=status.HTTP_201_CREATED)
