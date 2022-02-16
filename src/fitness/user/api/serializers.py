from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from ..models import *
from django.db import models
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password


class TraineeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainee
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

        def create(self, validated_data):
            trainee = Trainee.objects.create_user(validated_data['username'], password=validated_data['password'],
                                                  first_name=validated_data['first_name'],
                                                  last_name=validated_data['last_name'])
            return trainee