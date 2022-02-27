from django.contrib import admin
from django.urls import path, include

from base.views import users as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.registerUser, name='register'),
    path('profile/', views.getUserProfile, name='user-profile'),
    path('<str:pk>/', views.updateUserProfile, name='update-profile'),
    path('', views.UserList.as_view(), name='users'),
]