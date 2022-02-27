from django.urls import path
from base.views import trainers as views

urlpatterns = [

    path('', views.getTrainers, name="trainers"),

    path('create/', views.createTrainer, name="trainer-create"),
    path('upload/', views.uploadImage, name="image-upload"),

    path('<str:pk>/reviews/', views.createTrainerReview, name="create-review"),
    path('top/', views.getTopTrainers, name='top-trainers'),
    path('<str:pk>/', views.getTrainer, name='trainer'),

    # path('update/<str:pk>/', views.updateProduct, name="product-update"),
    path('delete/<str:pk>/', views.deleteTrainer, name="product-delete")
]