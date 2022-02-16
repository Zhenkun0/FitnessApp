from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions, mixins

from .serializers import *


# Register API
class TraineeRegisterApiView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TraineeSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trainee = serializer.save()
        return Response({
            "trainee": TraineeSerializer(trainee, context=self.get_serializer_context()).data,
            "message": "Trainee Created Successfully.  Now perform Login to get your token",
        })
