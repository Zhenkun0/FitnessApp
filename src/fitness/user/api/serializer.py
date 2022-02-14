from rest_framework import serializers
from ..models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class TraineeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trainee
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'height',
            'weight',
            'goal_setting',
            'dob',
            'gender',
        ]
        extra_kwargs = {'password': {'write_only': True, 'required': True}}
