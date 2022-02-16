import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fitness.settings')

from django import setup
setup()
from user.models import *

user = User.objects.get(pk=1)

t = Trainee(user=user)

t.save()