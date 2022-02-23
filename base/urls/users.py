from django.contrib import admin
from django.urls import path, include

from base.views import users as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.registerUser, name='register'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('', views.getUsers, name='users'),
    # path('trainers/', views.getTrainers, name='trainers'),
    # path('trainers/<str:pk>/', views.getTrainer, name='trainer'),
]