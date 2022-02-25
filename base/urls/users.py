from django.contrib import admin
from django.urls import path, include

from base.views import users as views

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.UserRegister.as_view(), name='register'),
    path('profile/', views.UserProfile.as_view(), name='user-profile'),
    path('', views.UserList.as_view(), name='users'),
]