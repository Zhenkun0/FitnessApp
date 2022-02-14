from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import TraineeSerializer


class CurrentTraineeAPIView(APIView):

    def get(self, request):
        serializer = TraineeSerializer(request.user)
        return Response(serializer.data)