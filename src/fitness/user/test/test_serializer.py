from django.test import TestCase

# Create your tests here.

from ..models import Trainee
from ..api.serializers import TraineeRegisterSerializer
from fitness import settings


class TraineeSerializerTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.trainee = Trainee.objects.create(user_name='test1', password='Passw0rd', email='test1@test.com')

    def test_get_serializer(self):
        serializer = TraineeRegisterSerializer(self.trainee)
        data = serializer.data
        self.assertEqual(data['user_name'], 'test1')
        self.assertEqual(data['email'], 'test1@test.com')

    def test_create_serializer(self):
        data = {
            'user_name': 'test2',
            'first_name': 'first',
            'last_name': 'last',
            'password': 'passw0rd',
            'email': 'test@test.com',
            'height': 6.2,
        }
        serializer = TraineeRegisterSerializer(data=data)
        serializer.is_valid()
        trainee = serializer.save()
        self.assertEqual(trainee.user_name, 'test2')
        self.assertEqual(trainee.password, 'passw0rd')
        self.assertEqual(trainee.height, 6.2)

    def test_create_serializer_with_error(self):
        data = {
            'user_name': 'test3',
        }
        serializer = TraineeRegisterSerializer(data=data)
        serializer.is_valid()
        # password, first, lastname, email are required
        self.assertEqual(len(serializer.errors), 4)
