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
            trainee = Trainee.objects.create_trainee(validated_data['username'],
                                                     password=validated_data['password'],
                                                     first_name=validated_data['first_name'],
                                                     last_name=validated_data['last_name'],
                                                     user_name=validated_data['user_name'],
                                                     email=validated_data['user_name'],
                                                     is_active=validated_data['is_active'],
                                                     is_staff=validated_data['is_staff'],
                                                     height=validated_data['height'],
                                                     weight=validated_data['weight'],
                                                     goal_setting=validated_data['goal_setting'],
                                                     dob=validated_data['dob'],
                                                     gender=validated_data['gender'],
                                                     )
            return trainee