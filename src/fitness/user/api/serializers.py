from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.db import models
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer


class TraineeRegisterSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
